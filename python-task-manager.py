#create the priotiy queue insertion
def insert(task_list, task):    
    task_list.append(task)

#define the priotiy queue (get highest priority)
def get_min_priority_index(task_list):
    
    lowest_priority_indx = 0
    lowest_priority = task_list[0][2] 
    for i in range(1,len(task_list)):
        if task_list[i][2] < lowest_priority:
            lowest_priority = task_list[i][2]
            lowest_priority_indx = i
    return lowest_priority_indx

#create the priotiy queue extraction
def extract(task_list):
    if len(task_list) == 0:
        return 
    lowest_priority_indx = get_min_priority_index(task_list)
    return task_list.pop(lowest_priority_indx)
 
#create the priotiy queue peek
def peek(task_list):
    if len(task_list) == 0:
        return
    lowest_priority_indx = get_min_priority_index(task_list)
    return task_list[lowest_priority_indx]

#check if the priority queue is empty
def is_empty(task_list):
    return len(task_list) == 0

#insert multiple tasks into the priority queue
def insert_task(task_list, num_tasks):
    for i in range(num_tasks):
        print("enter task", i+1, ":")
        name = str(input("Task a valid name: "))
        #validate task name
        while name == "":
            print("Task name cannot be empty. Please enter a valid name.")
            name = str(input("Task a valid name: "))
        duration = int(input("Duration(min):"))
        priority = int(input("Priority (lower number = higher priority): "))
        insert(task_list, (name, duration, priority))


# Function to extract the completed task from the priority queue
def complete_next_task(task_list):
    if is_empty(task_list):
        print("No tasks to complete.")
    else:
        task = extract(task_list)
        print("Completed task:", task)


#sort the task_list by task name before searching
def sort_tasks_by_name(task_list):
    for i in range(1, len(task_list)):
        key_task = task_list[i]
        j = i - 1
        while j >= 0 and task_list[j][0] > key_task[0]:
            task_list[j + 1] = task_list[j]
            j -= 1
        task_list[j + 1] = key_task
    return task_list
#search for a task using binary search
def search_for_task(task_list, search_task):
    # Sort the task list by name before binary search
    sort_tasks_by_name(task_list)
    low = 0
    high = len(task_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if task_list[mid][0] == search_task:
            return task_list[mid]
        elif task_list[mid][0] < search_task:
            low = mid + 1
        else:
            high = mid - 1

# Sort tasks by duration using insertion sort   
def sort_tasks(task_list): 
    for i in range(1, len(task_list)):
        key_task = task_list[i]
        key_duration = int(key_task[1])
        j = i - 1
        while j >= 0 and int(task_list[j][1]) > key_duration:
            task_list[j + 1] = task_list[j]
            j -= 1
        task_list[j + 1] = key_task
    return task_list

# Main program
print("Welcome to the Task Manager!")
print("enter the number of tasks you want to add:")
num_tasks=int(input())
task_list=[]

print("enter the task ,duration and priority for each task:")
insert_task(task_list, num_tasks)
print("Tasks added")


while not is_empty(task_list):
 print("Current tasks:")
 for task in task_list:
    print(task)
 print("what do you want to do next?")
 print("1. Complete next task")
 print("2. search a task")
 print("3.see the tasks from less duration to more duration")
 task_choice = input("Enter your choice (1/2/3): ")
 if task_choice == "1":
    complete_next_task(task_list)
 elif task_choice == "2":
    print("Enter the task you want to search:")
    search_task = input()
    search_for_task_result = search_for_task(task_list, search_task)
    if search_for_task_result is not None:
        print("Task found:", search_for_task_result)
    else:
        print("Task not found.")
 elif task_choice == "3":
    print("Tasks sorted by duration:")
    task_list = sort_tasks(task_list)
    for task in task_list:
        print(task)
 else:
    print("Invalid choice. Please try again.")


print("No more tasks to complete.")
print("Thank you for using the Task Manager!")