# Function to create students dictionary
def createStudentDict():
  dictStudent = {}
  n = int(input("Enter the number of students: "))
  for i in range(n):
    print("Enter the details of student", i + 1)
    name = input("Enter your name: ")
    roll = int(input("Enter your roll number: "))
    age = int(input("Enter your age: "))
    marks = int(input("Enter your marks: "))
    sec = input("Enter your section(BCA/BSc): ")
    infoTuple = (name, age, sec, marks)
    dictStudent[roll] = infoTuple
    if input("Do you want to exit(y/n): ") == "y":
      break
  return dictStudent


def saveToFile(dictStudent):
  with open("student_details.txt", "a") as file:
    for roll, details in dictStudent.items():
      file.write(f"Roll number: {roll}, Details: {details}\n")


def searchInFile():
  searchTerm = input("Enter the name or roll number to search in the file: ")
  with open("student_details.txt", "r") as file:
    for line in file:
      if searchTerm in line:
        print(line.strip())


def displayMenu():
  print("Menu:")
  print("1. Create a new student")
  print("2. Search for an existing student")
  print("3. Exit")


while True:
  displayMenu()
  choice = input("Enter your choice: ")

  if choice == "1":
    dictStudent = createStudentDict()
    saveToFile(dictStudent)
  elif choice == "2":
    searchInFile()
  elif choice == "3":
    print("Exiting the program.")
    break
  else:
    print("Invalid choice. Please select a valid option.")
