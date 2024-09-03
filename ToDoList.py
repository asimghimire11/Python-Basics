class Task:
    def __init__(self, title, description, status="pending"):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.title} ({self.status}): {self.description}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        title = input("Enter the task title: ")
        description = input("Enter the task description: ")
        status = input("Enter the task status (pending/ongoing/completed): ")
        while status not in ['pending', 'ongoing', 'completed']:
            print("Invalid status. Please enter either 'pending', 'ongoing', or 'completed'.")
            status = input("Enter the task status (pending/ongoing/completed): ")
        task = Task(title, description, status)
        self.tasks.append(task)
        print("Task added:", task)

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print("Task removed:", title)
                return
        print("Task not found in the list.")

    def view_tasks(self):
        if self.tasks:
            print("Todo List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Todo List is empty.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            todo_list.add_task()
        elif choice == '2':
            title = input("Enter the task title to remove: ")
            todo_list.remove_task(title)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

# Run the Todo List program
main()
