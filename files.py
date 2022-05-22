import os
directory = input("Please enter a directory: ")
file_name = input("Please enter the filename : ")
name = input("Please enter your name : ")
address = input("Please enter your address : ")
phone_num = input("Please enter your phone number : ")
if os.path.isdir(directory):
    writeFile = open(os.path.join(directory,file_name))
    writeFile.write(name+','+address+','+phone_num)
    writeFile.close()
    print("File contents:")
    readFile = open(os.path.join(directory,file_name))
    for line in readFile:
        print(line)
        readFile.close()
else:
    print("Sorry, the directory is not exists.")
