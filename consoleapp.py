import re
from FileHelper import write
dataset = []
def menu():
    print("-----------------------------------------")
    print("Welcome to Insight Workshop Academy")
    print("-----------------------------------------")

    print("Press 1 to enquiry courses list: ")
    print("Press 2 to add information of student: ")
    print("Press 3 to see information of student: ")
    print("Press 4 to update student information: ")
    print("Press 5 to delete student information: ")
    print("Press 6 to exit: ")

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
    full_name = str(input("Enter your name: "))
    email = input("Enter your email address: ")
    phone = int(input("Enter your phone number: "))
    selected_course = str(input("Enter course available in list: "))
    amount = float(input("Enter course amount: "))
    payment_on = int(input("Enter payment on: "))
    remaining = float(input("Enter your remainig amount: "))

    file = open('add_info.txt', 'a+')
    # for data in dataset:
        
    #     # file.writelines(full_name + '\t' + str(email) + '\t' + str(phone) + '\t' + selected_course + '\t' + str(amount) + '\t' + str(payment_on) + '\t' + str(remaining))
    file.write(full_name + ',' + str(email) + ',' + str(phone) + ',' + selected_course + ',' + str(amount) + ',' + str(payment_on) + ',' + str(remaining) + '\n')
    # content += '\n' 
    # file.write(content)
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
    obj2 = open("add_info.txt", "r")
    val=str(input("What do you want to update: "))
    old = raw_input("Enter old "+val+ ": " )
    new = raw_input("Enter new " + val + ": ")
    s = re.sub(old, new, obj2.read())
    obj1 = open("add_info.txt", "w")
    obj1.writelines(s)
    print("Successful")
update_info()

# def delete_info():
#     lines = list()
#     user_name = str(input("Enter student name to delete from file: "))

#     file.open("add_info.txt", 'r')
#     if user_name == name[0] 
while (True):
    menu()
    choice = input("Enter your choice: ")
    if (choice == '6'):
        exit()

    # elif(choice == '5'):
    #     delete_info()

    elif(choice == '4'):
        update_info()

    elif(choice == '3'):
        student_info()

    elif(choice == '2'):
        add_info()

    elif(choice == '1'):
        course_list()


