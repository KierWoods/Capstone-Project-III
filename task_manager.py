# Define functions reg_user, add_task, view_all, view_mine.
# Add functionality to "vm", number the tasks, give user ability to mark as complete
# and edit tasks.
# Allow access to task by using task number or exit to main menu by "-1"
# When editing task in "vm" username or task can be edited. Cannot edit complete task.
# Add "gr" generate report and "ds" display statistics to menu.
# Create txt files task_overview and user_overview and format accordingly.

# task_overview.txt to contain total tasks, number of tasks completed,
# number of tasks still to complete, overdue tasks, % of tasks not complete and % overdue.

# user_overview.txt must contain total number of users, total tasks, total tasks assigned to user
# % of tasks assigned to user, % of tasks completed by user, % not completed, % overdue.
# Add ability to print task_overview contents to user in "ds". 



# Define functions used throughout this program.
# Define reg_user, allow admin to register new users and other usernames print contact admin.

# Import datetime library 
from datetime import date

def reg_user():

    user_new = False
    confirm_pass = False

# If statement to confirm username is "admin".
    if username_enter == "admin":

# While loop to check username entered is not already stored in users.txt.
        while not user_new:
            new = True
            new_user = input("Please confirm your new username: ")
            if new_user == "":
                print("Please enter a username, your username can contain any characters")
            else:
                for i in range(0, len(user_list)):
                    if user_list[i][0] == new_user:
                        print("Username already in use, Please enter a different username!")
                        new = False
                if new:
                    user_new = True


                
        new_pass = input("Please create a new password: ")
        confirm_pass = input("Please confirm your new password: ")
        if confirm_pass == new_pass:
            with open('user.txt', 'a') as f:
                f.write("{}"", ""{}".format(new_user,new_pass))
        else:
            print("Please ensure your passwords match!")
    elif username_enter != admin_access:
        print("You do not have permission to register new users, Please contact admin") 
    return

# Define add_task; allow user to add tasks. 
def add_task():
    user_task = input("Please enter username of who will complete the task: ")
    task = input("Please enter task name: ")
    desc_task = input("Please enter a description of the task: ")
    due_date = input("Please input the date task is to be completed by: ")
    current_date = date.today()
    current_date = current_date.strftime("%d %b %Y")
    completion = "No"
    with open('tasks.txt', 'a') as f:
        f.write("{}, {}, {}, {}, {}, {}".format(user_task, task, desc_task, current_date, due_date, completion))
    print("Task Added")
    return

# Define function for user to view all tasks.
def view_all():
    with open("tasks.txt", "r") as f:
            for line in f.read().splitlines():
                words = line.split(", ")
                if len(words) == 6:
                    print("\n")
                    print('''Task:\t\t{}
Assigned to:\t{}
Date Assigned:\t{}
Due Date:\t{}
Task Complete?\t{}
Task Description:
{})'''.format(words[1], words[0],words[3], words[4], words[5], words[2]))

# Define function for user to view only their own tasks.
def view_mine():
    user_true = False
    task_list = []
    print("\nMy Task List")

# For loop to iterate through tasks. 
    for i in range(0, len(tasks)):
        if username_enter == tasks[i][0]:
            task_list.append(tasks[i])
            user_true = True

# True Conditional print the task list in specific format for user to view task(s) assigned.
    if user_true:
        for i in range(0, len(task_list)):
            print(f"\nTask {i+1}")
            print("Task:\t" + task_list[i][1])
            print("Assigned to:\t" + task_list[i][0])
            print("Date Assigned:\t" + task_list[i][3])
            print("Due Date:\t" + task_list[i][4])
            print("Task Complete?:\t" + task_list[i][5])
            print("Task Description:" + task_list[i][2])

# Menu options for user to edit task, return to main menu or complete task.
        while True:
# Return to main menu when -1 entered
                task_num = int(input("Please input Task number to edit or enter -1 to return to main menu: ")) 
                if task_num == -1:
                    break

# Elif task selection between 1 and highest task number.
                elif task_num > 0 and task_num <= len(task_list):                  
                     
# While loop for user to select option. 
                    while True:
                        sub_menu = input("""Menu
c - Mark task as complete.
e - Edit user assigned to task, task, task description and due date
-1 - Return to main menu.\n""")
                        

# If user selects "c" change "No" to "yes" in task_list. 
                        if sub_menu == "c":
                            task_list[task_num-1][5] = "Yes"
# Write to file.
                            with open("tasks.txt", "w") as task_new:
                                for task in task_list:
                                    task_line = task[0] + ", " + task[1] + ", " + task[2] + ", " + task[3] + ", " + task[4] + ", " + task[5] 
                                    task_new.write(task_line + "\n")
                                print(f"\nTask {task_num} has been marked as complete.")
                                break
# Return to main menu with "-1".
                        elif sub_menu == "-1":
                            return(menu)
                            

# Elif user selects "e" user input to edit user assigned task, task, task description and due date.
                        elif sub_menu == "e":
                            print(task_list[task_num-1])
                            if task_list[task_num-1][5] == "Yes":
                                print("\nThe task you have selected is already complete.")
                                break
                            elif task_list[task_num-1][5] == "No":
                                print("\nPlease enter the Username, Task,Task Description and Due Date")
                                username = input("Enter new username:\t\t\t")
                                new_task = input("Enter new task:\t\t\t")
                                new_desc = input("Enter new task description:\t\t")
                                due_date = input("Enter new Date Due for completion:\t")
                                
# User input must contain a value, replace list items with user input. 
                                if username != "":
                                    task_list[task_num-1][0] = username
                                if new_task != "":
                                    task_list[task_num-1][1] = new_task 
                                if new_desc != "":
                                    task_list[task_num-1][2] = new_desc
                                if due_date != "":
                                    task_list[task_num-1][4] = due_date
                             

                            print("\n Informtion Updated! Please check tasks.txt")
                            print("Username:\t\t" + task_list[task_num-1][0])
                            print("Task:\t\t\t" + task_list[task_num-1][1])
                            print("Task Description:\t" + task_list[task_num-1][2])
                            print("Due Date:\t\t" + task_list[task_num-1][4])
# Write to task.txt file.
                            with open("tasks.txt", "w") as task_new:
                                print(task_list)
                                for task in task_list:
                                    task_line = task[0] + ", " + task[1] + ", " + task[2] + ", " + task[3] + ", " + task[4] + ", " + task[5]
                                    print(task_line)
                                    print(task)
                                    task_new.write(task_line + "\n")
                               

                            break
                        
# If user input is not recognised, print error message. 
                        else:
                            print("Please Select option from above.")         

# Inform user no tasks assigned to username.
    if not user_true:
        print("No tasks found for selected user.")



                    

 

# Read username and password from txt file and store in list.
# Split list at ", " username and password nwo separate. 
in_file = open('user.txt', 'r')
user_list = in_file.read().splitlines()
user_list = [i.strip().split(", ") for i in user_list]
in_file.close()

# Open and store tasks.txt as variable.
task = open ("tasks.txt", "r+")
tasks = task.readlines()
tasks = [i.strip().split(", ") for i in tasks]

# Request username and password.
username_true = False
password_true = False

# While loop to determine entry is stored in users.txt.
# If True allow access. 
while not username_true:
    username_enter = input("Username:\n")
    for i in range(0, len(user_list)):
        if user_list[i][0] == username_enter:
            username_true = True
            
# Password verification if True, determine password is stored in users.txt.
        if username_true:
            while not password_true:
                password_enter = input("Password:\n")
                if user_list[i][1] == password_enter:
                    password_true = True
                if not password_true:
                    print("Please enter the correct password")
        else:
            print("Please enter correct username")       
                



# Display specific menu if admin is logged in. 
admin_access = ("admin")
if username_enter == admin_access:

# Presenting menu to the user.
# Ensure that the user input is converted to lower case.
# Conditional statement for use of the menu function.
    while True:
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds- display statistics
e - Exit
: ''').lower()
    

# Register new username and password.  Verify passwords match then store to users.txt.
# Conditional statement to verify passwords match.  If not print message to user.
        if menu == 'r':
           reg_user()

# Give user the ability to add tasks and store in tasks.txt file.
        elif menu == 'a':
            add_task()
            
# User can view all tasks stored on tasks.txt.
# Print in clear format as described in PDF.
        elif menu == 'va':
            view_all()

# Allow user to view tasks assigned to their username only.
# Format and print to user in appropriate format as described in pdf.
        elif menu == 'vm':
           view_mine()

              
# Allow user to exit program once finsihed. 
        elif menu == 'e':
            print('Goodbye!!!')
            exit()


# Add "ds" display statistics menu for admin user only.
# Count and display total users and total tasks to user in requested format. 
        elif menu == "ds":
            print("Statistics")
            print("Statistics report from file:\n")
            user_stats = open("user_overview.txt", "r") 
            while True: # for loop 
                line = user_stats.readline()
                if not line:
                    break;
                print(line.strip())
            user_stats.close()
            task_stats = open("task_overview.txt", "r")
            while True:
                line = task_stats.readline()
                if not line:
                    break;
                print(line.strip())
            task_stats.close()


# Add "gr" generate reports for admin only.
        elif menu == "gr":
            print("Generate Reports")         
                                         
# Declare variables for task_overview.
            total_task = len(tasks)
            task_yes = 0
            task_no = 0
            task_overdue = 0
            percentage_yes = 0
            percentage_no = 0
            percentage_overdue = 0

# Loop through task and count complete/ incomplete.
            for i in range(0, len(tasks)):
                if tasks[i][5] == "Yes":
                    task_yes += 1
                elif tasks[i][5] == "No":
                    task_no += 1
                    
# Use datetime conditional to determine how many tasks are overdue. 
                    due_date = datetime.strptime(tasks[i][4], "%d %b %Y")
                    if datetime.date(datetime.now()) > due_date.date():
                        task_overdue += 1

            if total_task == 0:
                percentage_no = 0
                precentage_overdue = 0
                percentage_yes = 0 
            else:
                percentage_no = round(task_no * 100 / total_task)
                percentage_overdue = round(task_overdue * 100 / total_task)
                percentage_yes = round(task_yes * 100 / total_task)

# Write tasks report to task_overview.txt, labelled and formatted.
            with open("task_overview.txt", "w+") as task_overview:
                task_overview.write(f"""Task Overview\n
Number of tasks:\t{total_task}
Number of Tasks Complete:\t{task_yes}
Tasks Complete %:\t{percentage_yes}
Number of Tasks Incomplete:\t{task_no}
Tasks incomplete %:\t{percentage_no}
Number of Tasks Overdue:\t{task_overdue}
Tasks Overdue %:\t{percentage_overdue}
""")
# Create/open user_overview.txt and write report to it.
            with open ("user_overview.txt", "w+") as user_overview:
                
                for i in range(0, len(user_list)):
# Declare variables for user_overview.
                    total_users = 0
                    total_task = 0
                    total_task_user = 0
                    task_yes = 0
                    task_no = 0
                    task_overdue = 0
                    percentage_user_assign = 0 
                    percentage_user_complete = 0
                    percentage_user_incomplete = 0
                    percentage_user_overdue = 0
                    users = len(user_list)
                    total_task = len(tasks)

# Write to useroverview title, and report for each user. 
                    user_overview.write(f"""\n\t\t\tUser Overview Report
Users Registered: {users}
Tasks Generated: {total_task}\n""")
                    user_overview.write(f"\nUser:\t{user_list[i][0]}\n")
                    
# Loop through tasks and confirm assigned to user and task status; complete/incomplete and overdue.
                    for b in range(0, len(tasks)):
                        if user_list[i][0] == tasks[b][0]:
                            total_users += 1
                            if tasks[b][5] == "Yes":
                                task_yes += 1
                            elif tasks[b][5] == "No":
                                task_no =+ 1
                                date_incomplete = datetime.strptime(tasks[i][4], "%d %b %Y")
                                if datetime.date(datetime.now()) < due_date.date():
                                    task_overdue += 1
 # Calculate % for reports.                           
                    if total_task == 0:
                        percentage_user_incomplete = 0
                        percentage_user_overdue = 0
                        percentage_user_complete = 0

                    else:
                        percentage_user_complete = round(task_yes * 100 / total_task)
                        percentage_user_incomplete = round(task_no * 100 / total_task)
                        percentage_user_overdue = round(task_overdue * 100 / total_task)

                    if total_task == 0:
                        percentage_user_assign = 0
                    else:
                        percentage_user_assign = round(total_users * 100 / total_task)

# Write data to file for each user.
                    user_overview.write(f"""User Tasks:\t{total_users}\n
Task(s) Assigned to user %:\t{percentage_user_assign}
Task(s) Completed %:\t\t{percentage_user_complete}
Task(s) Incomplete %:\t\t{percentage_user_incomplete}
Task(s) Overdue %:\t\t{percentage_user_overdue}""")

# Inform user where to find inofrmation and that process has been actioned. 
                    print("""Reports generated;

task_overview.txt
user_overview.txt

Please open these files to check reports.\n""")

# Error message to when erronous input is entered for the menu. 
        else:
            print("You have made a wrong choice, Please Try again")
       

# Present menu to user.  Ensure that the user input is converted to lower case.
else:
    while True:
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()
    

# Register new username and password.  Verify passwords match then store to users.txt.
# Conditional statement to verify passwords match.  If not print message to user.
        if menu == 'r':
           reg_user()

# Give user the ability to add tasks and store in tasks.txt file.
        elif menu == 'a':
           add_task()

# User can view all tasks stored on tasks.txt.
# Print in clear format as described in PDF.
        elif menu == 'va':
            view_all()

# Allow user to view asks assigned to their username only.
# Format and print to user in appropriate format as described in pdf.
        elif menu == 'vm':
            view_mine()
            
              
# Allow user to exit program once finsihed. 
        elif menu == 'e':
            print('Goodbye!!!')
            exit()
        
# Error message to when erronous input is entered for the menu. 
        else:
            print("You have made a wrong choice, Please Try again")
    
