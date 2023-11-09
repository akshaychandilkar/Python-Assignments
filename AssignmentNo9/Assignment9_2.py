import os 

def main():
    print("Enter the file name : ")
    file_name = input()
    
    if os.path.exists(file_name):
        fobj = open(file_name,"w")  # write mode 
        if fobj:
            print("Contents of the file : ")
            Data = input()

            fobj.write(Data)  # write the data into the file

            fobj.close()
        else:
            print("Unable to open file")
    else:
        print("There is no such file")
    
if __name__ == "__main__":
    main()