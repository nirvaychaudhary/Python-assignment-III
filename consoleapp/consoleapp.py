import re
from FileHelper import write
dataset = []
def menu():
    print("-----------------------------------------")
    print("Welcome to Insight Workshop Academy")
    print("-----------------------------------------")

    print("-----------------------------------------")
    print("Press 1 to enquiry courses list: ")
    print("-----------------------------------------")
    print("Press 2 to add information of student: ")
    print("-----------------------------------------")
    print("Press 3 to see information of student: ")
    print("-----------------------------------------")
    print("Press 4 to update student information: ")
    print("-----------------------------------------")
    print("Press 5 to delete student information: ")
    print("-----------------------------------------")
    print("Press 6 to exit: ")
    print("-----------------------------------------")

def course_list():
    print("---------------")
    print("Courses list")
    print("---------------")
    dataset = []
    file = open('coursedata.txt', 'r')
    for line in file.readlines():
        tokens = line.split(',')
        dataset.append(tokens)
    print("------------------------------------------------------------------")
    print("id \t name \t duration")
    print("------------------------------------------------------------------")
    for data in dataset:
        print(data[0] + '\t' + data[1] + '\t' + data[2])

def add_info():
    print("----------------------------")
    print("add student information")
    print("----------------------------")
    full_name = str(input("Enter student name: "))
    email = input("Enter student email address: ")
    phone = int(input("Enter student phone number: "))
    selected_course = str(input("Enter course available in list: "))
    amount = float(input("Enter course amount: "))
    payment_on = int(input("Enter payment on: "))
    remaining = float(input("Enter your remainig amount: "))

    
    file = open('add_info.txt', 'a+')
    
    file.write(full_name + ',' + str(email) + ',' + str(phone) + ',' + selected_course + ',' + str(amount) + ',' + str(payment_on) + ',' + str(remaining) + '\n')
    
    file.close()

def student_info():
    print("-------------------")
    print("show all Student information")
    print("-------------------")
    for line in open('add_info.txt', 'r'). readlines():
        tokens = line.split(',')
        dataset.append(tokens)

    content = '--------------------------------------------------------------------------------------\n'
    content += 'full_name \t email \t phone \t selected_course \t amount \t payment_on \t remaining\n'
    content += '--------------------------------------------------------------------------------------\n'
    print(content)
    
    data_content = ''
    for data in dataset:
        data_content += data[0] + '\t' + data[1] + '\t' + data[2] + '\t' + data[3] + '\t' + data[4] + '\t' + data[5] + '\t' + data[6] + '\n'

    print(data_content)
    write('report.txt', content + data_content)

def update_info():
    
    val = str(input("What you want to update: "))
    old = input("Enter old "+val+ ": " )
    new = input("Enter new " + val + ": ")
    
    f = open('report.txt', 'r+')
    f2 = open('updated_report.txt', 'a+')
    text = f.read()
    text = re.sub(old, new, text)
    f.seek(0)
    f.close()
    f2.write(text)
    f2.close()

def delete_info():
    # lines = list()
    name = input("Please enter full name to delete student name: ")
    with open('add_info.txt', 'r') as myfile:
        readfile = myfile.readlines()
        i=1
        for i in range(i, len(readfile)+1):
            if readfile[i-1].split(',')[0] == name:
                readfile.pop(i)
                print(readfile)
    #             lines.append(row)
    #             print("Sucessfully deleted")
        #     else:
        #             print("Please enter correct name to delete! ")
        #             break
        # myfile = open('report.txt', 'a')
        # # myfile.close()
   


while (True):
    menu()
    choice = input("Enter your choice: ")
    if (choice == '6'):
        exit()

    elif(choice == '5'):
        delete_info()

    elif(choice == '4'):
        update_info()

    elif(choice == '3'):
        student_info()

    elif(choice == '2'):
        add_info()

    elif(choice == '1'):
        course_list()


