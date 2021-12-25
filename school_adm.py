import csv
def write_into_csv(info):
    with open('studentinfo.csv','w+', newline='') as csv_f1:
        stuwriter= csv.writer(csv_f1)
        stuwriter.writerow(info)

while True:
    stuinfo=input("Enter student info as (NAME AGE CONTACT EMAIL):")
    print("Enter info:", str(stuinfo))

    stuinfolist=stuinfo.split(" ")
    print("Entered split info is :", str(stuinfolist))

    write_into_csv(stuinfolist)

    check=input("Enter if you want to enter info about another student(y/n):")
    if check=='y':
        True
    elif check=='n':
        False
