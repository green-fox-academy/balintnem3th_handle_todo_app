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

    def list_all_the_tasks(self):
     if len(self._argument_list) == 2 and self._argument_list[1] == '-l':
            print('\n')
            task_order = 1
            my_file = open(self._stored_data, "r")
            if os.stat('data.txt').st_size == 0:
                print("No todos for today! :)")
            else:
                for line in my_file:
                    print(str(task_order) + ' - ' + line,end ='')
                    task_order +=1

    def add_new_task(self):
     if len(self._argument_list) > 2 and self._argument_list[1] == '-a':
            print('\n')
            write_list = []
            my_file = open(self._stored_data, "w")
            for index in range(2,len(self._argument_list)):
                write_list.append(self._argument_list[index])
            with open("data.txt", "a") as myfile:
                for lines in write_list:
                    my_file.write(lines+ '\n')

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
         
         

             
        
    



list_task = lists_tasks()
if len(sys.argv) == 1:
    list_task.print_usage()
if len(sys.argv) == 2 and sys.argv[1] == '-l':
    list_task.list_all_the_tasks()
if len(sys.argv) > 2 and sys.argv[1] == '-a':
    list_task.add_new_task()
if len(sys.argv) == 2  and sys.argv[1] == '-a':
    list_task.error_handling()
if len(sys.argv) == 3  and sys.argv[1] == '-r' :
    list_task.remove_task()