import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="180725",
    database="pdbc_test"
    )
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        age INT NOT NULL)''')
    connection.commit()
    return connection
def create_user(connection):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
    connection.commit()
    print("User added successfully!")

def read_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    if users:
        print("\nID\tName\tAge")
        print("-" * 20)
        for user in users:
            print(f"{user[0]}\t{user[1]}\t{user[2]}")
    else:
        print("No users found.")

def update_user(connection):
    user_id = int(input("Enter user ID to update: "))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    if user:
        name = input(f"Enter new name (current: {user[1]}): ") or user[1]
        age = input(f"Enter new age (current: {user[2]}): ") or user[2]
        cursor.execute("UPDATE users SET name = %s, age = %s WHERE id = %s", (name, age, user_id))
        connection.commit()
        print("User updated successfully!")
    else:
        print("User not found.")

def delete_user(connection):
    user_id = int(input("Enter user ID to delete: "))
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    connection.commit()
    if cursor.rowcount:
        print("User deleted successfully!")
    else:
        print("User not found.")

def menu():
    connection = connect_db()
    while True:
        print("\n--- MENU ---")
        print("1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_user(connection)
        elif choice == '2':
            read_users(connection)
        elif choice == '3':
            update_user(connection)
        elif choice == '4':
            delete_user(connection)
        elif choice == '5':
            connection.close()
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please select a valid option.")
menu()
    
