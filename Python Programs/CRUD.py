# CRUD python script in indonesia (Translated)
# script to put what have you done

done = []

def selesai(): #done
    if (len(done) <= 0):
        print ('NOT FOUND')
    else:
        for i in range(len(done)):
            print(i,done[i])

def masuk(): #put
    baru = input('Masukkan yang sudah selesai : ') #put anything you have done
    done.append(baru)


def ubah(): #change
    selesai()
    i = int(input('Masukkan id : ')) #put the id which you wanna change
    if (len(done) < i):
        print('INVALID')
    else:
        sls = input('apa yg sudah dilakukan : ') #put what have you done
        done[i] = sls
        

def hapus(): #delete
    selesai()
    i = int(input('Masukkan ID : ')) #put id which you wanna delete
    if (len(done) < i):
        print('INVALID')
    else:
        done.remove(done[i])

def menu():
    print('\n')
    print('='*15,'MENU','='*15)
    print('[1] LIST')
    print('[2] ADD')
    print('[3] CHANGE')
    print('[4] DELETE')
    print('[5] EXIT')

    menu = int(input('Pilih menu : ')) #choose menu
    print('\n')

    if(menu == 1):
        selesai()
    elif(menu==2):
        masuk()
    elif(menu==3):
        ubah()
    elif(menu==4):
        hapus()
    elif(menu==5):
        exit()
    else:
        print('TIDAK TERSEDIA') #NOT FOUND

if __name__ == "__main__":
    while(True):
        menu()