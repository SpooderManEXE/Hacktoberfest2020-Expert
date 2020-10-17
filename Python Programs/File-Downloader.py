import wget

url = input("Enter The File URL: ")
YN = input("Do you want to give specific name for file Y/N: ")

if YN == 'Y':
    name = input("Give your File name: ")
    print("File Downloading ....")
    wget.download(url, name)

else:
    print("File Downloading ....")
    wget.download(url)

print("\n File Downloaded")
