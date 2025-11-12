''' here are all the functions required in the main file '''
# list of all options
list_opts = ["a", "d", "e", "v", "E"]

# this function is to give options of operations available to user
def give_options() -> str:
    print("")
    print("Operations Available : ")
    print(f"\tTo Add a new task - {list_opts[0]}")
    print(f"\tTo Delete a task - {list_opts[1]}")
    print(f"\tTo Edit a task - {list_opts[2]}")
    print(f"\tTo View all existing tasks - {list_opts[3]}")
    print(f"\tTo Exit - {list_opts[4]} or 'random text'")

    print("")

    user_opt: str = input("What would you like to do among the above options, choose any one : ")
    print("")

    return user_opt

# this function is to add a new task to the list
def add_task() -> None:
    new_task: str = input("Enter the new task: ")

    print("Adding task...")

    with open("D:\\Python_Programming\\Mini_Projects\\ToDo_List_Manager\\tasks_history.txt", "a") as f:
        f.write(f"{new_task}\n")

    print("Added Successfully !!")

# this function is to delete a task
def delete_task() -> None:
    with open("D:\\Python_Programming\\Mini_Projects\\ToDo_List_Manager\\tasks_history.txt", "r") as f:
        all_tasks = [task for task in f.readlines()]

    for i in range(0, len(all_tasks)):
        print(f"{i+1}. {all_tasks[i]}")

    print("")

    to_del_task: int = int(input("Select the task you want to delete by writing its respective srno: "))

    all_tasks.pop((to_del_task - 1))

    print("Deleting...")
    with open("D:\\Python_Programming\\Mini_Projects\\ToDo_List_Manager\\tasks_history.txt", "w") as f:
        for task in all_tasks:
            f.write(task)

    print("Deletion Successful !!")

# this function is to edit a task
def edit_task() -> None:
    with open("D:\\Python_Programming\\Mini_Projects\\ToDo_List_Manager\\tasks_history.txt", "r") as f:
        all_tasks = [task for task in f.readlines()]

    for i in range(0, len(all_tasks)):
        print(f"{i+1}. {all_tasks[i]}")

    print("")

    to_del_task: int = int(input("Select the task you want to edit by writing its respective srno: "))

    new_task: str = input("New Task: ")

    all_tasks[(to_del_task - 1)] = new_task

    with open("D:\\Python_Programming\\Mini_Projects\\ToDo_List_Manager\\tasks_history.txt", "w") as f:
        for task in all_tasks:
            f.write(task)

    print("Editing Successful !!")

# this function is to view all tasks
def view_tasks() -> None:
    with open("D:\\Python_Programming\\Mini_Projects\\ToDo_List_Manager\\tasks_history.txt", "r") as f:
        all_tasks = [task.strip() for task in f.readlines()]

    for i in range(0, len(all_tasks)):
        print(f"{i+1}. {all_tasks[i]}")

    print("")
    print("These are all the task you have !!")
