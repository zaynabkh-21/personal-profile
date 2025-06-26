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
 
