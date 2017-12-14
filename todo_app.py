import sys
import error_handling
import os



class lists_tasks(object):

    def __init__(self):
        self._argument_list = sys.argv
        self._stored_data = 'data.txt'

    def print_usage(self):
        if len(self._argument_list) == 1:
            print('\n')
            print("Command Line Todo application")
            print("=============================")
            print('\n')
            print("Command line arguments:")
            print("-l   Lists all the tasks")
            print("-a   Adds a new task")
            print("-r   Removes an task")
            print("-c   Completes an task")

    def list_all_the_tasks_1(self):
     if len(self._argument_list) == 2 and self._argument_list[1] == '-l':
            print('\n')
            my_file = open(self._stored_data, "r+")
            if os.stat('data.txt').st_size == 0:
                print("No todos for today! :)")
            else:
                for lines in my_file:
                    print(lines)

    def add_new_task(self):
     if len(self._argument_list) > 2 and self._argument_list[1] == '-a':
            print('\n')
            write_list = []
            not_checked = '- [ ] '
            task_order = 1
            index_x = 0
            my_file = open(self._stored_data, "r+")
            for lines in my_file:
                write_list.append(lines)
                index_x +=1
                print('myfile 1:'+ lines)
            for index in range(2,len(self._argument_list)):
                write_list.append(self._argument_list[index])
            with open("data.txt", "a") as myfile:
               
                for index in range(index_x,len(write_list)): 
                    variable = (str(task_order)+ not_checked )
                    my_file.write(variable + lines+ '\n') 
                    task_order += 1
          

    def error_handling(self):
     if len(self._argument_list) == 2  and self._argument_list[1] == '-a':
            print('\n')
            print("Error Message:" )
            print('\n')
            print("Unable to add: no task provided")

    def remove_task(self):
     if len(self._argument_list) == 3  and self._argument_list[1] == '-r' :
         remove_line = self._argument_list[2]
         new_list = []
         my_file = open(self._stored_data, "r")
         for lines in my_file:
            new_list.append(lines)
         new_list.pop(int(remove_line)-1)
         my_file.close()
         with open(self._stored_data, 'w') as f:
            for line in new_list:
                f.write(line.rstrip() + '\n')
         
         
            '''     def check_task(self):
         if len(self._argument_list) == 3  and self._argument_list[1] == '-c' :
             checked = self._argument_list[3]



        def remove_error_handling(self):
            sum_line = 0
            my_file = open(self._stored_data, "r")
            for line in my_file:
                sum_line += 1
            if len(self._argument_list) == 2  and self._argument_list[1] == '-r' :
                print('\n')
                print("Unable to remove: no index provided")
            elif len(self._argument_list) == 3  and self._argument_list[1] == '-r' and self._argument_list[2]< sum_line :
                print('\n')
                print("index is out of bound")
            elif len(self._argument_list) == 3  and self._argument_list[1] == '-r' and (type(self._argument_list[2]) != type(1)):
                print('\n')
             print("index is not a number")'''

    

    
    
    



list_task = lists_tasks()
if len(sys.argv) == 1:
    list_task.print_usage()
if len(sys.argv) == 2 and sys.argv[1] == '-l':
    list_task.list_all_the_tasks_1()
if len(sys.argv) > 2 and sys.argv[1] == '-a':
    list_task.add_new_task()
if len(sys.argv) == 2  and sys.argv[1] == '-a':
    list_task.error_handling()
if len(sys.argv) == 3  and sys.argv[1] == '-r' :
    list_task.remove_task()
#else:
#    lists_tasks.remove_error_handling()




