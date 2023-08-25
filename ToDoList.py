import csv


def addTask():      # Add a task in csv file

    task = input("Add a task on your to-do list: ")
    lastRowId = 0
    with open('ToDoList.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            lastRowId = int(row[0])

    lastRowId += 1
    lastRowIdStr = str(lastRowId)
    with open('ToDoList.csv', mode='a') as file:
        file.write(lastRowIdStr + "," + task + ',n\n')
    return
    

def showTask():     # Show the list and mark a cross if it's done

    print("\n To-Do List:\n")
    with open('ToDoList.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[2] == 'n'): # Not done
                print(row[0] + ". [ ] " + row[1])
            elif(row[2] == 'y'): # Done 
                print(row[0] + ". [X] " + row[1])


def markDoneTask():     # Change the n to a y in the csv
    
    showTask()
    taskToMark = input("Which one ? ")
    data = []

    # Read all csv
    with open('ToDoList.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    # Find the row to change
    for row in data:
        if row[0] == taskToMark:
            # Mark it done
            row[2] = 'y'

    # Write the new line 
    with open('ToDoList.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def deleteTask():       # Delete a row on the csv

    showTask()
    taskToDelete = input("Which one ? ")

    data = []

    # Read all csv
    with open('ToDoList.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    # Find the row to delete
    found = False
    updated_data = []
    for row in data:
        if row[0] == taskToDelete:
            found = True
        else:
            updated_data.append(row)

    # Écrire les données modifiées dans le fichier
    with open('ToDoList.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_data)



def main():     # Main

    while (True):   # Won't stop until user uses Leave option
        print("\n\n***To-Do List***\n")

        print("1. Add task")
        print("2. Show tasks")
        print("3. Mark done task")
        print("4. Delete task")
        print("5. Leave")

        choice = int(input("Choose your option: "))

        if choice == 1:
            addTask()
        elif choice == 2:
            showTask()
        elif choice == 3:
            markDoneTask()
        elif choice == 4:
            deleteTask()
        elif choice == 5:
            exit()
        else:
            print("Non-valid number, try again")
    

main()