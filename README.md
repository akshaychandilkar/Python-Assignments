# Python-Assignments Questions 

# Assignment 1
1. Write a program which contains one function named as Fun(). That function should display "Hello from Fun" on console.
2. Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display "Even number" otherwise display "Odd number" on console.
Input: 11     Input: 8       Output: Odd Number      Output: Even Number
3. Write a program which contains one function named as Add() which accepts two numbers. from user and return addition of that two numbers.
Input: 11 5       Output: 16
4. Write a program which display 5 times Marvellous on screen.
Output: Marvellous   Marvellous   Marvellous    Marvellous    Marvellous
5. Write a program which display 10 to 1 on screen. 9 8 7 6 5 4
Output: 10 9 8 7 6 5 4 3 2 1
6. Write a program which accept number from user and check whether that number is positive or negative or zero.
Input: 11 Input: -8   Input: 0     Output:Positive Number   Output: Negative Number  Output: Zero   
7. Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
Input: 25  Input: 8    Output: False    Output: True
8. Write a program which accept number from user and print that number of "*" on screen.
Input: 5   Output: * * * * * 
9.Write a program which display first 10 even numbers on screen.
Output:2 4 6 8 10 12 14 16 18 20
10. Write a program which accept name from user and display length of its name.
Input: Marvellous      Output: 10
Note:For each above question please create separate.py file as
Assignment1_1.py        Assignment1_2.py     Assignment1 3.py
Every applications logic should be enclosed in function.

# Assignment 2
1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.
2. Write a program which accept one number and display below pattern.
Input: 5
3. Write a program which accept one number from user and return its factorial.
Input: 5      Output: 120
4. Write a program which accept one number form user and return addition of its factors.
Input:12     Output: 16    (1+2+3+4+6)
5. Write a program which accept one number for user and check whether number is prime or not.
Input: 5      Output: It is Prime Number
6. Write a program which accept one number and display below pattern.
Input: 5   
7. Write a program which accept one number and display below pattern.
Input: 5
8. Write a program which accept one number and display below pattern.
Input: 5
9. Write a program which accept number from user and return number of digits in that number.
Input: 5187934     Output:7
10. Write a program which accept number from user and return addition of digits in that number.
Input: 5187934     Output: 37
Note:
For each above question please create separate.py file as
Assignment2_1.py     Assignment2_2.py    Assignment2_3.py
Every applications logic should be enclosed in function

# Assignment 3
1. Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
Input: Number of elements: 6     Input Elements: 13  5  45  7  4  56   Output: 130
2. Write a progr program which accept N numbers from user and store it into List. Return Maximum number from that List.
Input: Number of elements: 7     Input Elements: 13  5  45  7  4  56  34     Output: 56
3. Write a program which accept N numbers from user and store it into List. Return Minimum. number from that List.
Input: Number of elements: 4     Input Elements: 13  5  45  7      Output: 5
4. Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
Input: Number of elements: 11    Input Elements: 13  5  45  7  4  56  5  34  2  5  65   Element to search: 5      Output: 3
5. Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().
Input: Number of elements: 11    Input Elements: 13  5  45  7  4  56  10  34  2  5  8     Output: 54 (13+5+7+2+5)

# Assignment 4
1. Write a program which contains one lambda function which accepts one parameter and return power of two.
Input: 4     Input: 6       Output: 16      Output: 64
2. Write a program which contains one lambda function which accepts two parameters and return its multiplication.
Input: 4 3   Input: 6 3    Output: 12     Output: 18
3. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]     List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]                           Output of reduce = 6538752000
4. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]    List after filter =  [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]        Output of reduce = 204
5. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).
Input List = [2, 70, 11, 10, 17, 23, 31, 77]          List after filter = [2, 11, 17, 23, 31]
List after map =  [4, 22, 34, 46, 62]                 Output of reduce = 62

# Assignment 5
1. Write a program which contains one class named as Demo. Demo class contains two instance variables as nol, по2. That class contains one class variable as Value.
There are two instance methods of class as Fun and Gun which displays values of instance variables.Initialise instance variable in init method by accepting the values from user.
After creating the class create the two objects of Demo class as
Obj1 Demo(11,21)   Obj2 Demo(51,101)
Now call the instance methods as
Obj1.Fun()    Obj2.Fun()     Obj1.Gun()    Obj2.Gun()
2. Write a program which contains one class named as Circle.
Circle class contains three instance variables as Radius, Area, Circumference. That class contains one class variable as PI which is initialise to 3.14.
Inside init method initialise all instance variables to 0.0. There are three instance methods inside class as Accept(), Calculate Area(), CalculateCircumference(), Display(). Accept method will accept value of Radius from user.
CalculateArea() method will calculate area of circle and store it into instance variable Area. CalculateCircumference() method will calculate circumference of circle and store it into instance. variable Circumference. And Display() method will display value of all the instance variables as Radius, Area, Circumference. After designing the above class call all instance methods by creating multiple objects.
3. Write a program which contains one class named as Arithmetic.
Arithmetic class contains three instance variables as Value1,Value2. Inside init method initialise all instance variables to 0.
There are three instance methods inside class as Accept(), Addition(), Subtraction(), Multiplication(), Division().
Accept method will accept value of Valuel and Value2 from user. Addition() method will perform addition of Value1, Value2 and return result. Subtraction() method will perform subtraction of Valuel, Value2 and return result. Multiplication() method will perform multiplication of Valuel, Value2 and return result. Division() method will perform division of Value1, Value2 and return result. After designing the above class call all instance methods by creating multiple objects.

# Assignment 6
1. Write a program which contains one class named as BookStore. BookStore class contains two instance variables as Name, Author.
That class contains one class variable as NoOfBooks which is initialise to 0. There is one instance methods of class as Display which displays name, Author and number of books.
Initialise instance variable in init method by accepting the values from user as name and author. Inside init method increment value of NoOfBooks by one.
After creating the class create the two objects of BookStore class as
Obj1 BookStore ("Linux System Programming", "Robert Love")           Obj1. Display() #Linux System Programming by Robert Love. No of books: 1
Obj2 = BookStore("C Programming", "Dennis Ritchie")                  Obj2.Display() # C Programming by Dennis Ritchie. No of books: 2
2. Write a program which contains one class named as BankAccount. BankAccount class contains two instance variables as Name & Amount.
That class contains one class variable as ROI which is initialise to 10.5.
Inside init method initialise all name and amount variables by accepting the values from user. There are Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateIntrest(). Deposit() method will accept the amount from user and add that value in class instance variable Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount. CalculateIntrest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI. And Display() method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects.
3. Write a program which contains one class named as Numbers. Arithmetic class contains one instance variables as Value
4. Inside init method initialise that instance variables to the value which is accepted from user. There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(), Factors(). ChkPrime() method will returns true if number is prime otherwise return false. ChkPerfect() method will returns true if number is perfect otherwise return false.
Factors() method will display all factors of instance variable. SumFactors() method will return addition of all factors. Use this method in any another method as a helper method if required.
After designing the above class call all instance methods by creating multiple objects.

# Assignment 7 
1. Design python application which creates two thread named as even and odd. Even thread will display first 10 even numbers and odd thread will display first 10 odd numbers.
2. Design python application which creates two threads as evenfactor and oddfactor. Both the thread accept one parameter as integer. Evenfactor thread will display addition of even factors of given number and oddfactor will display addition of odd factors of given number. After execution of both the thread gets completed main thread should display message as "exit from main".
3. Design python application which creates two threads as evenlist and oddlist. Both the threads accept list of integers as parameter. Evenlist thread add all even elements from input list and display the addition. Oddlist thread add all odd elements from input list and display the addition.
4. Design python application which creates three threads as small, capital, digits. All the threads accepts string as parameter. Small thread display number of small characters, capital thread display number of capital characters and digits thread display number of digits. Display id and name of each thread.
5. Design python application which contains two threads named as thread1 and thread2. Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on screen. After execution of thread1 gets completed then schedule thread2.

# Assignment 8
1. Write a recursive program which display below pattern.
Input: 5        Output: *  *  *  *  *
2. Write a recursive program which display below pattern.
Input: 5        Output:1  2  3  4  5
3. Write a recursive program which display below pattern.
Input: 5        Output:5  4  3  2  1
4. Write a recursive program which accept number from user and return summation of its digits.
Input : 879     Output: 24
5. Write a recursive program which accept number from user and return its factorial.
Input: 5        Output: 120

# Assignment 9
1. Write a program which accepts file name from user and check whether that file exists in current directory or not.
Input: Demo.txt
Check whether Demo.txt exists or not.
3. Write a program which accept file name from user and open that file and display the contents of that file on screen.
Input: Demo.txt
Display contents of Demo.txt on console.
4. Write a program which accept file name from user and create new file named as Demo.txt and copy all contents from existing file into new file. Accept file name through command line. arguments.
Input: ABC.txt
Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt
5. Write a program which accept two file names from user and compare contents of both the files. If both the files contains same contents then display success otherwise display failure. Accept names of both the files from command line.
Input: Demo.txt       Hello.txt
Compare contents of Demo.txt and Hello.txt
6. Accept file name and one string from user and return the frequency of that string from file..
Input: Demo.txt      Marvellous
Search "Marvellous" in Demo.txt

# Assignment 10
Please follow below rules while designing automation script as
• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function. • For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.
1. Design automation script which accept directory name and file extension from user. Display all files with that extension.
Usage: DirectoryFileSearch.py "Demo" ".txt"
Demo is name of directory and .txt is the extension that we want to search.
2. Design automation script which accept directory name and two file extensions from user. Rename all files with first file extension with the second file extenntion.
Usage: DirectoryRename.py "Demo" ".txt"".doc"
Demo is name of directory and txt is the extension that we want to search and rename with.doc. After execution this script each .txt file gets renamed as .doc.
3. Design automation script which accept two directory names. Copy all files from first directory into second directory. Second directory should be created at run time.
Usage: DirectoryCopy.py "Demo" "Temp"
Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and copy all files from Demo to Temp.
4. Design automation script which accept two directory names and one file extension. Copy all files with the specified extension from first directory into second directory. Second directory should be created at run time.
Usage: Directory CopyExt.py "Demo" "Temp" ".exe"
Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and copy all files with extension .exe from Demo to Temp

# Assignment 11
Please follow below rules while designing automation script as
• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.
1. Design automation script which accept directory name and display checksum of all files.
Usage: DirectoryChecksum.py "Demo"
Demo is name of directory.
2. Design automation script which accept directory name and write names of duplicate files from that directory into log file named as Log.txt. Log.txt file should be created into current directory.
Usage DirectoryDusplicate.py "Demo"
Demo is name of directory.
3. Design automation script which accept directory name and delete all duplicate files from that directory. Write names of duplicate files from that directory into log file named as Log.txt. Log.txt file should be created into current directory.
Usage: Directory DusplicateRemoval.py "Demo"
Demo is name of directory.
4. Design automation script which accept directory name and delete all duplicate files from that directory. Write names of duplicate files from that directory into log file named as Log.txt. Log.txt file should be created into current directory. Display execution time required for the script.
Usage: Directory DusplicateRemoval.py "Demo"
Demo is name of directory.


# Assignment 12
Please follow below rules while designing automation script as
• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function. • For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality..
1. Design automation script which display information of running processes as its name, PID, Username.
Usage: ProcInfo.py
2. Design automation script which accept process name and display information of that process if it is running.
Usage: ProcInfo.py Notepad
3. Design automation script which accept directory name from user and create log file in that directory which contains information of running processes as its name, PID, Username,
Usage: ProcInfoLog.py Demo
Demo is name of Directory.
4. Design automation script which accept directory name and mail id from user and create log file in that directory which contains information of running processes as its name, PID, Username. After creating log file send that log file to the specified mail.
Usage: ProcInfoLog.py Demo akshaychandilkar@gmail.com
Demo is name of Directory. akshaychandilkar@gmail.com is the mail id.


# Assignment 13
Please follow below rules while designing automation script as
• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function. • For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.
Design automation script which performs following task.
Accept Directory name from user and delete all duplicate files from the specified directory by
considering the checksum of files. Create one Directory named as Marvellous and inside that directory create log file which maintains all names of duplicate files which are deleted.
Name of that log file should contains the date and time at which that file gets created. Accept duration in minutes from user and perform task of duplicate file removal after the specific time interval.
Accept Mail id from user and send the attachment of the log file.
Mail body should contains statistics about the operation of duplicate file removal.
Mail body should contains below things:
    Starting time of scanning 
    Total number of files scanned
    Total number of duplicate files found
Consider below command line options for the gives script
DuplicateFileRemoval.py E:/Data/Demo 50 akshaychandilkar@gmail.com
DuplicateFileRemoval.py
    Name of python automation script
-E:/Data/Demo
    Absolute path of directory which may contains duplicate files.
- 50
   Time interval of script in minutes.
- akshaychandilkar@gmail.com
   Mail ID of the receiver
Note:
For every separate task write separate function.
Write all user defined functions in one user defined module.
Use proper validation techniques.
Provide Help and usage option for script. Create one Readme file which contains description of our script, details of command line options.
