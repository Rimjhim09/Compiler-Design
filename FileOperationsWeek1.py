import csv


student_records = ['Roll_No.', 'Name', 'marks_sub1', 'marks_sub2', 'marks_sub3']
student_CSV_file = 'week 1.csv'


def display_menu():
    print("\n********************************************")
    print("[+] Welcome to Student Management System [+]")
    print("********************************************\n")
    print("1. Add New Student")
    print("2. Delete Records")
    print("3. View Records")
    print("4. Update Records")
    print("5. Calculte Total")
    print("6. Quit")


def add_record():
    print("\n*******************************")
    print("[+] Add Student Information [+]")
    print("*******************************\n")
    
    global student_records
    global student_CSV_file

    student_data = []
    for field in student_records:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_CSV_file, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return



def view_records():
    print("\n***********************************")
    print("[+] Display Student Information [+]")
    print("***********************************\n")
    global student_records
    global student_CSV_file

    

    with open(student_CSV_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_records:
            print((str(x)).center(30), end='|')
        print()
        print("".center(155,"_"))
        print()
        for row in reader:
            for item in row:
                print((str(item)).center(30), end="|")
            print("\n")

    input("Press any key to continue")



def update_record():
    global student_records
    global student_CSV_file

    print("\n**********************************")
    print("[+] Update Student Information [+]")
    print("**********************************\n")

    roll = input("Enter roll no. to update: ")
    index_student = None
    updated_data = []
    with open(student_CSV_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student Found at index:",index_student)
                    student_data = []
                    for field in student_records:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    
    if index_student is not None:
        with open(student_CSV_file, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Roll No. not found in our database")

    input("Press any key to continue")


def delete_record():
    global student_records
    global student_CSV_file

    print("\n**********************************")
    print("[+] Delete Student Information [+]")
    print("**********************************\n")

    
    roll = input("Enter roll no. to delete: ")
    student_found = False
    updated_data = []
    with open(student_CSV_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_CSV_file, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Roll no. ", roll, "deleted successfully")
    else:
        print("Roll No. not found in our database")

    input("Press any key to continue")


def cal_records():
    print("\n***********************************")
    print("[+] Display Student's Total Marks [+]")
    print("***********************************\n")
    global student_records
    global student_CSV_file

    

    with open(student_CSV_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        

        for row in reader:
            if (len(row)>0):
                print(row[0],"\t",row[1],"\t","Sum: ",int(row[2])+int(row[3])+int(row[4]), end="\t")
            print("\n")

    input("Press any key to continue")


while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_record()
    elif choice == '2':
        delete_record()
    elif choice == '3':
        view_records()
    elif choice == '4':
        update_record()
    elif choice == '5':
        cal_records()
    elif choice == '6':
        break
    else:
        print("\nInvalid input, retry again...")
        continue

print("\n*******************************")
print(" Thank you for using our system")
print("*******************************\n")
