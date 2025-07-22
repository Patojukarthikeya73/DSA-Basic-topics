try:
    filename= input("Enter the file name: ")
    file= open(filename, 'r')
    print("Number from file", Number)
    file.close()
except FileNotFoundError:
    print("File doesnot exist")
except ValueError:
    print("File does not have integer.......")
except:
    print("Unkown  Error....")
    