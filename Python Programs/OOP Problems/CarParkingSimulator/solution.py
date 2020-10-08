import math
from datetime import datetime, timedelta

from abc import ABC, abstractmethod


class CarPark:
    _carHalfHourlyRates: list = [[700, 1900, 0.6], [1900, 2230, 0.8]]
    _carNightCharge: float = 5
    _motorBikeCharges: list = [[700, 2230, 0.65]]
    _motorBikeNightCharge: list = 0.7
    _nextId = 1

    def __init__(self, address):
        self._carparkId = CarPark._nextId
        CarPark._nextId += 1
        self._address = address

    def address(self):
        return self._address

    @property
    def carParkId(self):
        return self._carparkId

    def _filterHourlyRate(self, hourlyRates, aTime):
        for rate in hourlyRates:
            if rate[0] <= aTime < rate[1]:
                return rate
        return None

    def getCarHalfHourlyRate(self, aTime):
        return self._filterHourlyRate(self._carHalfHourlyRates, aTime)

    def getMotorBikeCharge(self, aTime):
        return self._filterHourlyRate(self._motorBikeCharges, aTime)

    def getCarNightCharge(self):
        return self._carNightCharge

    def getMotorBikeNightCharge(self):
        return self._motorBikeNightCharge

    def __str__(self):
        return F'Id: {self._carparkId} {self._address} **Outside of Central Area**'


class CentralAreaCarPark(CarPark):
    _nightParkingSurcharge: float = 2
    _carHalfHourlyRates = [[700, 1700, 1.2], [1700, 2320, 0.9]]

    def __init__(self, address, factor):
        super().__init__(address)
        self._factor = factor

    def factor(self):
        return self._factor

    def setFactor(self, newFactor):
        self._factor = newFactor

    def getNightParkingSurcharge(self):
        return self._nightParkingSurcharge

    def setNightParkingSurcharge(self, nightParkingSurcharge: float):
        self._nightParkingSurcharge = nightParkingSurcharge

    def getCarNightCharge(self):
        return super(CentralAreaCarPark, self).getCarNightCharge() + self.getNightParkingSurcharge()

    def getCarHalfHourlyRate(self, aTime):
        rate = super(CentralAreaCarPark, self).getCarHalfHourlyRate(aTime)
        if rate:
            rate[2] = rate[2] * self._factor
            return rate
        return None

    def __str__(self):
        return f'Carpark Id: {self._carparkId} Factor: {self._factor} {self._address} **Within Central Area**'


class ParkingCalculator(ABC):

    def calculateCharge(self, timeIn, timeOut, carpark: CarPark):

        differenceInMinutes = (timeOut - timeIn).total_seconds() / 60
        if differenceInMinutes <= 10:
            return 0

        totalCharge = 0.0
        startTime = timeIn

        while startTime < timeOut:
            startTimeRate = self.getDayRate(int(startTime.strftime('%H%M')), carpark)
            intermediateEndTime = (startTime + timedelta(hours=1)).replace(minute=0)  # reach to start of next hour
            intermediateTimeRate = self.getDayRate(int(intermediateEndTime.strftime('%H%M')), carpark)

            while intermediateEndTime < timeOut and startTimeRate == intermediateTimeRate:
                intermediateEndTime = (intermediateEndTime + timedelta(hours=1)).replace(minute=0)
                intermediateTimeRate = self.getDayRate(int(intermediateEndTime.strftime('%H%M')), carpark)

            if startTimeRate is None:
                totalCharge += self.getNightRate(carpark)
                if intermediateEndTime > timeOut:
                    break
                startTime = intermediateEndTime.replace(
                    hour=int((intermediateTimeRate[0])/100),
                    minute=(intermediateTimeRate[0] % 100)
                )
            else:
                endTime = startTime.replace(
                    hour=int((startTimeRate[1])/100), minute=(startTimeRate[1] % 100)
                ) if not intermediateEndTime > timeOut else timeOut

                totalCharge += self.getCharges(endTime, startTime, startTimeRate[2])
                startTime = endTime

        return totalCharge

    @abstractmethod
    def getDayRate(self, startTime, carpark: CarPark):
        pass

    @abstractmethod
    def getNightRate(self, carpark: CarPark):
        pass

    @abstractmethod
    def getCharges(self, endTime, startTime, rate):
        pass


class CarParkingCalculator(ParkingCalculator):
    def getDayRate(self, startTime, carpark: CarPark):
        return carpark.getCarHalfHourlyRate(startTime)

    def getNightRate(self, carpark: CarPark):
        return carpark.getCarNightCharge()

    def getCharges(self, endTime, startTime, rate):
        return math.ceil((((endTime - startTime).total_seconds() / 60) / 30)) * rate


class MotorbikeParkingCalculator(ParkingCalculator):
    def getDayRate(self, startTime, carpark: CarPark):
        return carpark.getMotorBikeCharge(startTime)

    def getNightRate(self, carpark: CarPark):
        return carpark.getMotorBikeNightCharge()

    def getCharges(self, endTime, startTime, rate):
        return math.ceil((((endTime - startTime).total_seconds() / 60) / 60)) * rate


class ParkingException(Exception):
    pass


class ParkingDetailException(ParkingException):

    def __init__(self, parking):
        self._parking = parking

    def parking(self):
        return self._parking


class Vehicle:

    def __init__(self, vehicleNumber, type):
        self._vehicleNumber = vehicleNumber
        self._type = type

    @property
    def vehicleNumber(self):
        return self._vehicleNumber


class Parking(ABC):
    _calculator: CarParkingCalculator = None

    def __init__(self, carpark, timeIn, vehicle):
        self._timeIn: datetime = timeIn
        self._timeOut = None
        self._charges = 0.00
        self._vehicle = vehicle
        self._carpark = carpark

    def __str__(self):
        timeOutString = f'Time Out: {f"*Parked in carpark {self._carpark.carParkId}" if not self._timeOut else self._timeOut}'
        chargesString = f'$ {"0.00" if not self._timeOut else self._charges}'
        return f'Time In: {self._timeIn}, {timeOutString} Charges: {chargesString} \n {self._carpark} \n Vehicle: {self._vehicle.vehicleNumber}'

    def timeIn(self):
        return self._timeIn

    def carPark(self):
        return self._carpark

    @property
    def timeOut(self):
        if not self._timeOut:
            raise ParkingException('Car has not left Parking as yet')
        return self._timeOut

    @timeOut.setter
    def timeOut(self, timeout):
        if self._timeOut:
            raise ParkingException('Time out has already been recorded')
        elif timeout < self._timeIn:
            raise ParkingException('Time out cannot be earlier than time in!')
        self._timeOut = timeout
        self._charges = round(self._calculator.calculateCharge(self._timeIn, self._timeOut, self._carpark), 2)

    @property
    def charges(self):
        if not self._timeOut:
            raise ParkingException('Charges not recorded yet as vehicle has not left carpark')
        return self._charges

    def is_parked(self):
        return not bool(self._timeOut)

    @property
    def vehicle(self):
        return self._vehicle


class MotorBikeParking(Parking):
    _calculator = MotorbikeParkingCalculator()

    def __init__(self, carpark, timeIn, vehicle):
        super(MotorBikeParking, self).__init__(carpark, timeIn, vehicle)

    def __str__(self):
        return super().__str__() + ' Motor Bike\n'


class CarParking(Parking):
    _calculator = CarParkingCalculator()

    def __init__(self, carpark, timeIn, vehicle):
        super(CarParking, self).__init__(carpark, timeIn, vehicle)

    def __str__(self):
        return super().__str__() + ' Car\n'


class CarParkTrackingSystem:

    def __init__(self):
        self._carparks = list()
        self._parkings = list()

    def searchCarParkById(self, carParkId: int):
        for carpark in self._carparks:
            if carpark.carParkId == carParkId:
                return carpark
        return None

    def searchCarParkByAddress(self, address: str):
        for carpark in self._carparks:
            if carpark.address() == address:
                return carpark
        return None

    def addCarpark(self, carpark):
        if self.searchCarParkByAddress(carpark.address):
            return False
        self._carparks.append(carpark)
        return True

    def getParkingByVehicleNumber(self, vehicleNumber, currentOnly=True):
        parkingsByVehicleNumber = [parking for parking in self._parkings if
                                   parking.vehicle.vehicleNumber == vehicleNumber]
        if currentOnly:
            parkingsByVehicleNumber = [parking for parking in parkingsByVehicleNumber if parking.is_parked()]

        return parkingsByVehicleNumber

    def getParkingByCarpark(self, carparkId, currentOnly=True):
        parkingsByCarpark = [parking for parking in self._parkings if parking.carPark().carParkId == carparkId]

        if currentOnly:
            parkingsByCarpark = [parking for parking in parkingsByCarpark if parking.is_parked()]

        return parkingsByCarpark

    def isVehicleParked(self, vehicle):
        return bool(self.getParkingByVehicleNumber(vehicleNumber=vehicle.vehicleNumber))

    def addParking(self, parking):
        activeParking = self.getParkingByVehicleNumber(vehicleNumber=parking.vehicle.vehicleNumber)
        if activeParking:
            raise ParkingDetailException(parking=activeParking[0])

        self._parkings.append(parking)
        return True

    def listParkingByAllCarpark(self):
        totalActiveParkings = 0
        totalParkingAmount = 0.00

        for carpark in self._carparks:
            print(f'\nDetail of carpark {carpark} \n')

            totalCompletedParkingsByCarPark = 0
            totalChargesByCarPark = 0.00
            carparkParkings = self.getParkingByCarpark(carparkId=carpark.carParkId, currentOnly=False)

            for parking in carparkParkings:
                print(parking)
                if not parking.is_parked():
                    totalCompletedParkingsByCarPark += 1
                    totalChargesByCarPark += parking.charges
            print(f'Number of completed parking: {totalCompletedParkingsByCarPark}\n')
            print(
                f'Number of vehicles parked in carpark currently: {len(carparkParkings) - totalCompletedParkingsByCarPark}\n')
            print(f'Total amount: ${totalChargesByCarPark}\n')
            totalParkingAmount += totalChargesByCarPark
            totalActiveParkings += totalCompletedParkingsByCarPark

        print('Summary for all carparks\n')
        print(f'Total collected: ${totalParkingAmount}\n\n')
        print(f'Number of vehicles parked in all carparks currently: {totalActiveParkings}\n')


class CarParkApplication:
    _MENU = """1. Park a Vehicle \n2. Exit Carpark \n3. Display Parking Summary for all Carparks\n4.Exit\nEnter option:"""
    _MENU_OPTIONS = range(1, 5)
    _VEHICLE_TYPE_MENU = "Enter type of parking 1 - Car  2 - Motor bike"
    _DATE_INPUT_MENU = "Enter time {} in dd/mm/yyyy hh:mm AM/PM format:"
    _CAR_PARK_OPTIONS = {1: CarParking, 2: MotorBikeParking}
    _VEHICLE_OPTIONS = _CAR_PARK_OPTIONS.keys()
    _DATE_TYPE_FORMAT = '%d/%m/%Y %H:%M %p'

    def __init__(self):
        self._carSystem = CarParkTrackingSystem()
        self._carSystem.addCarpark(CarPark('11A Clementi Ave 12'))
        self._carSystem.addCarpark(CentralAreaCarPark('23 Syed Ameen Road', 1.1))
        self.getMenuInput()

    def _printMenu(self):
        print(self._MENU)

    def _validateMenuInput(self, inputCommand):
        return inputCommand.isdigit() and int(inputCommand) in self._MENU_OPTIONS

    def _validateVehicleTypeInput(self, inputCommand):
        return inputCommand.isdigit() and int(inputCommand) in self._VEHICLE_OPTIONS

    def _validateDateInput(self, dateIn):
        try:
            datetime.strptime(dateIn, self._DATE_TYPE_FORMAT)
        except ValueError:
            return False
        else:
            return True

    def _handleExistingParking(self, oldParking: Parking, newParking: Parking):
        print('Do you want to exit the vehicle for this parking? y/n: ')
        exitCarPark = input()
        if not exitCarPark.isalpha() and exitCarPark not in ('y', 'n'):
            print('Invalid input')
            return False

        if exitCarPark == 'n':
            print('Choosing not to exit previous parking')
            return False

        oldParking.timeOut = datetime.now()
        print(f'charges: {oldParking.charges}')

        self._carSystem.addParking(newParking)
        print(f'{newParking} *added \n')

        return True

    def _parkCarMenu(self, parkingType):
        print('Enter carpark id:')
        carParkId = input()

        if not carParkId.isdigit():
            print('carpark id should be an integer')
            return False
        carPark = self._carSystem.searchCarParkById(int(carParkId))

        if not carPark:
            print('carpark id does not belong to any carpark')
            return False

        print('Enter vehicle number: ')
        vehicleNumber = input()

        timeIn = self._getTimeAsInput()

        vehicle = Vehicle(vehicleNumber, parkingType)
        parking = CarParking(carPark, timeIn, vehicle) if parkingType == 1 else MotorBikeParking(
            carPark, timeIn, vehicle
        )

        try:
            self._carSystem.addParking(parking=parking)
        except ParkingDetailException as e:
            print('Error in adding a parking. Parking record shows vehicle is still in a carpark')
            print(e.parking())
            return self._handleExistingParking(e.parking(), parking)
        else:
            print(f'{parking} *added \n')
        return True

    def _getParkingTypeAsInput(self):
        print(self._VEHICLE_TYPE_MENU)
        parkType = input()
        while not self._validateVehicleTypeInput(parkType):
            print('Parking type is not a correct parking type. \n ')
            print(self._VEHICLE_TYPE_MENU)
            parkType = input()
        return int(parkType)

    def _getTimeAsInput(self, timeIn=True):
        print(self._DATE_INPUT_MENU.format('in' if timeIn else 'out'))
        dateTime = input()
        while not self._validateDateInput(dateTime):
            print('Not in correct dd/mm/yyyy hh:mm AM/PM  format \n')
            print(self._DATE_INPUT_MENU.format('in' if timeIn else 'out'))
            dateTime = input()
        return datetime.strptime(dateTime, self._DATE_TYPE_FORMAT)

    def _exitCarPark(self):
        print('Enter vehicle number: ')
        vehicleNumber = input()
        parkingToExit = self._carSystem.getParkingByVehicleNumber(vehicleNumber)
        if not parkingToExit:
            print('No existing parking with this vehicle number')
            return

        print(parkingToExit[0])
        timeOut = self._getTimeAsInput(timeIn=False)

        try:
            parkingToExit[0].timeOut = timeOut
        except ParkingException as e:
            print(e)
        else:
            print(f'charges ${parkingToExit[0].charges}')

    def getMenuInput(self):
        exit = False

        while not exit:
            self._printMenu()
            inputCommand = input()

            while not self._validateMenuInput(inputCommand):
                self._printMenu()
                inputCommand = input()

            inputCommand = int(inputCommand)

            if inputCommand == 1:
                parkingType = self._getParkingTypeAsInput()
                self._parkCarMenu(parkingType)
            elif inputCommand == 2:
                self._exitCarPark()
            elif inputCommand == 3:
                self._carSystem.listParkingByAllCarpark()
            elif inputCommand == 4:
                exit = True
            else:
                print('Invalid Input Try again ! \n')


def main():
    CarParkApplication()


if __name__ == "__main__":
    main()

