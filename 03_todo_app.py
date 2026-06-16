import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect("todos.db")
cursor = conn.cursor()

# Create the table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        done INTEGER DEFAULT 0
    )
""")
conn.commit()

def add_task(task):
    cursor.execute("INSERT INTO todos (task) VALUES (?)", (task,))
    conn.commit()
    print(f"Task '{task}' added.")

def view_tasks():
    cursor.execute("SELECT * FROM todos")
    tasks = cursor.fetchall()
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for task in tasks:
            status = "✓" if task[2] == 1 else "✗"
            print(f"{task[0]}. [{status}] {task[1]}")

def complete_task(task_id):
    cursor.execute("UPDATE todos SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    print(f"Task {task_id} marked as complete.")

def delete_task(task_id):
    cursor.execute("DELETE FROM todos WHERE id = ?", (task_id,))
    conn.commit()
    print(f"Task {task_id} deleted.")

while True:
    print("\n--- Todo App ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_id = int(input("Enter task ID to complete: "))
        complete_task(task_id)
    elif choice == "4":
        task_id = int(input("Enter task ID to delete: "))
        delete_task(task_id)
    elif choice == "5":
        print("Goodbye!")
        conn.close()
        break
    else:
        print("Invalid choice")