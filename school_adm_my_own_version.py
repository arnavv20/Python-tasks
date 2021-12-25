import csv
f= open('studentinfo.csv','w+',newline='')
stuwriter=csv.writer(f)
stuwriter.writerow(['Name','Age','Contact Number','Email'])
n=int(input("Enter the number of students you want to enter info about:"))

ans='y'

while ans=='y':
    for i in range(n):
        print("Student Record",(i+1))
        name=input("Enter name")
        age=int(input("Enter age"))
        contactno=int(input("Enter number"))
        email=input("Enter your email id")
        sturec=[name, age, contactno, email]
        stuwriter.writerow(sturec)
    ans=input("Want more records?(y/n)")
f.close
