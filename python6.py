import os

class TodoList:
    def __init__(self):
        self.tasks = {}
        self.task_id = 1
    
    def add_task(self, description):
        self.tasks[self.task_id] = {"description": description, "completed": False}
        self.task_id += 1
        print(f"Task '{description}' added successfully!")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            print("Your To-Do List:")
            for task_id, task in self.tasks.items():
                status = "Completed" if task["completed"] else "Pending"
                print(f"{task_id}. {task['description']} - {status}")
    
    def mark_completed(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]["completed"] = True
            print(f"Task {task_id} marked as completed!")
        else:
            print("Task not found.")
    
    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task {task_id} deleted!")
        else:
            print("Task not found.")
    
    def save_tasks(self, filename):
        try:
            with open(filename, 'w') as f:
                for task_id, task in self.tasks.items():
                    status = "Completed" if task["completed"] else "Pending"
                    f.write(f"{task_id},{task['description']},{status}\n")
            print(f"Tasks saved to {filename}.")
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def load_tasks(self, filename):
        if not os.path.exists(filename):
            print("No saved tasks found.")
            return
        try:
            with open(filename, 'r') as f:
                for line in f:
                    task_id, description, status = line.strip().split(',')
                    task_id = int(task_id)
                    completed = status == "Completed"
                    self.tasks[task_id] = {"description": description, "completed": completed}
                    self.task_id = max(self.task_id, task_id + 1)
            print(f"Tasks loaded from {filename}.")
        except Exception as e:
            print(f"Error loading tasks: {e}")
    
    def show_menu(self):
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("7. Exit")
    
    def get_choice(self):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice in range(1, 8):
                    return choice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 7.")
    
    def run(self):
        while True:
            self.show_menu()
            choice = self.get_choice()
            if choice == 1:
                description = input("Enter task description: ")
                self.add_task(description)
            elif choice == 2:
                self.view_tasks()
            elif choice == 3:
                task_id = int(input("Enter task ID to mark as completed: "))
                self.mark_completed(task_id)
            elif choice == 4:
                task_id = int(input("Enter task ID to delete: "))
                self.delete_task(task_id)
            elif choice == 5:
                filename = input("Enter filename to save tasks: ")
                self.save_tasks(filename)
            elif choice == 6:
                filename = input("Enter filename to load tasks: ")
                self.load_tasks(filename)
            elif choice == 7:
                print("Goodbye!")
                break

if __name__ == "__main__":
    todo = TodoList()
    todo.run()
