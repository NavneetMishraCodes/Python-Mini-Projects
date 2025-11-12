''' In this time.sleep() is just used to make the terminal app more real '''
# importing required files and modules
import functions as fn

# introducing the ToDo List Manager
print("Welcome To ToDo List Manager...")

# main loop
while True:
    selected_opt = fn.give_options()
    
    if selected_opt in fn.list_opts:
        if selected_opt == 'a':
            fn.add_task()
        
        elif selected_opt == 'd':
            fn.delete_task()

        elif selected_opt == 'e':
            fn.edit_task()

        elif selected_opt == 'v':
            fn.view_tasks()
        
        else:
            print("Exiting the ToDo List Manager...")
            exit()


    else:
        print("Exiting the ToDo List Manager...")
        exit()
