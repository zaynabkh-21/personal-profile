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
        name = input("Task a valid name: ")
        duration = input("Duration(min):")
        priority = int(input("Priority (lower number = higher priority): "))
        insert(task_list, (name, duration, priority))


# Function to extract the completed task from the priority queue
def complete_next_task(task_list):
    if is_empty(task_list):
        print("No tasks to complete.")
    else:
        task = extract(task_list)
        print("Completed task:", task)

#search for a task using binary search
def search_for_task(task_list, search_task):
    low=0
    high=len(task_list)-1
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
