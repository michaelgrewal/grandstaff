# Michael Grewal


''' This program manages client records for a music school. '''

def readFile(filename):
    ''' This function reads a csv file containing all the student information and returns it as a 2D grid.'''

    try:
        #setup
        grid = []                       #initialze empty list
        f = open(filename, 'r')         #open the csv file in read mode
        raw = f.readlines()             #read every line as a list of strings

        #read each line of raw data and turn them into lists
        for i in range(1,len(raw)):
            line = raw[i]
            line = line.replace('\n','')
            line = line.split(',')

            #cast numbers values to integers
            for j in range(len(line)):
                if line[j].isdigit():
                    line[j]=int(line[j])

            #append the processed list into the 2D grid
            grid.append(line)

        f.close()
        return grid
    
    except:

        #tell user csv was not found and promt to initialize a new database
        print("\nSorry, .csv file could not be found.\
            \nIf this is your first time running the program, please initialize...")
        user = input("INITIALIZE NEW DATABASE? YES/NO: ").upper()

        #create an empty csv
        if user == "YES":
            f = open('grandstaff.csv','w')
            f.write("F.NAME,L.NAME,AGE,INST,CREDS"+"\n")
            f.close()
            print("\n***INITIALIZE SUCCESSFUL***")
            return readFile('grandstaff.csv')

        else:
            exit()



def createStudent(filename):
    ''' This function takes a filename as argument and creates a profile for new students by 
    writing their information to a csv file. '''

    try:
        #ask user to input information pertaining to student
        print("")
        print("Please enter the new student's information.")

        #first name input
        while True:
            fName = input('First Name: ').title()
            if fName.replace(' ','').isalpha() == True:
                break
            else:
                print("Sorry, numbers and symbols are not permitted.")
        
        #last name input
        while True:
            lName = input('Last Name: ').title()
            if lName.replace(' ','').isalpha() == True:
                break
            else:
                print("Sorry, numbers and symbols are not permitted.")

        #age input
        while True:
            age = input('Age: ')
            if age.isdigit() == True and 0<int(age)<100:
                break
            else:
                print("Sorry, that's not a valid age.")

        #instrument selection
        while True:
            validInstruments = ['Piano','Guitar','Drums','Voice']
            instrument = input('Instrument (Piano, Guitar, Drums, or Voice): ').title()
            if instrument not in validInstruments:
                print("Sorry, this school does not offer lessons for that instrument.")
            else:
                break

        #number of credits i.e. lessons paid for
        while True:
            paidCredits = input('Credits (1 Credit is 30min): ')
            if paidCredits.isdigit() == True and int(paidCredits)>0:
                break
            else:
                print("Sorry, only numbers are permitted.")
        
        #confirm and write the student information to the csv file
        while True:

            #display the inputted information and promt to save
            displayTable([[fName,lName,age,instrument,paidCredits]])
            user = input("\nConfirm and save?\
                \n> ").upper()

            #if explicitly 'YES'/'Y' then add the student info and save file
            if user == 'Y' or user == 'YES':
                f = open(filename, 'a')
                f.write(fName+','+lName+','+age+','+instrument+','+paidCredits+'\n')
                f.close()
                print("\n*****SAVE SUCCESSFUL*****")
                break
            
            #if explicitly 'NO'/'N' then don't save and move on
            elif user == 'N' or user == 'NO':
                print("\n#####INFO WAS NOT SAVED#####")
                break
            
    except:
        print("Sorry, someting went wrong while creating the new student.")



def displayTable(grid):
    ''' This function takes a 2D grid as argument and displays all student information stored 
    in the grid in a neatly formatted table. '''

    #setup
    space = ''
    bars = '===='

    #print header
    print("")
    print(f"F.Name{space:6}L.Name{space:6}Age{space:5}Inst{space:4}Creds{space:3}")
    print(bars*12)

    #print each student's information stored in the grid
    for i in range(len(grid)):
        output = f"{grid[i][0]:12}"             #init output with student's name

        for j in range(1,len(grid[i])):
            output += str(grid[i][j])+'\t'      #concatenate all other info to output

        print(output)


def menu():
    ''' This function displays the main menu and returns the user's selection. '''
    
    #print header
    print("")
    print(" -----------\n| Main Menu |\n -----------\n")

    #print selections
    selection = input("[1] Display student records\
        \n[2] Create a new student\
        \n[3] Add or remove credits\
        \n[4] Modify student information\
        \n[9] Help\
        \n[0] Quit\
        \n> ")

    return selection



def studentCredits(grid):
    ''' This function takes the 2D grid as argument and allows the user to modify the number of 
    credits on the student's account. '''

    #ask user to choose a student
    print("Which Student?: ")
    fName = input("First Name: ").title()
    lName = input("Last Name: ").title()

    #find that student in the grid
    counter = 0
    for i in range(len(grid)):

        #if student is found then give the choice to add or remove credits
        if grid[i][0] == fName and grid[i][1] == lName:
            choice = input("Type 'add _' or 'remove _' to modify credits. \
                \n> ")
            counter += 1
            number = ''

            for c in choice:
                if c.isdigit() == True:
                    number += c
            
            #add or remove credits on appropriate grid cell
            if 'add' in choice:
                grid[i][4] += int(number)
            elif 'remove' in choice:
                grid[i][4] -= int(number)
    
    #if name was not found print a message
    if counter == 0:
        print(f"Could not find the student {fName} {lName}.")



def modifyStudent(grid):
    ''' This function will modify elements of student's information. '''
    pass



def saveWork(filename,grid):
    ''' This function overwrites the csv file with updated student information. '''

    #setup
    f = open(filename,'w')
    output = "F.NAME,L.NAME,AGE,INST,CREDS\n"

    #create output string data for writing to file
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if j == len(grid[i])-1:
                output += str(grid[i][j])+'\n'
            else:
                output += str(grid[i][j])+','
    
    #save work
    f.write(output)
    print("\n*****SAVE SUCCESSFUL*****")
    f.close()



def filterByInst(grid,instrument):
    ''' This function takes a 2D grid containing student information and returns new list filtered
    by instrument. '''

    #setup
    filteredList = []

    #search the grid for students with the instrument
    for i in range(len(grid)):

        #if student with instrument found then append it to a new list
        if grid[i][3] == instrument:
            filteredList.append(grid[i])
    
    return filteredList



def filterByFName(grid,fName):
    ''' This function takes a 2D grid containing student information and returns new list filtered
    by first name. It also accepts partial entries ('Mich' will return Michael and Michelle)'''

    #setup
    filteredList = []

    #search the grid for students with the instrument
    for i in range(len(grid)):

        #if student with instrument found then append it to a new list
        if fName in grid[i][0]:
            filteredList.append(grid[i])
    
    return filteredList



def filterByLName(grid,lName):
    ''' This function takes a 2D grid containing student information and returns new list filtered
    by last name. '''

    #setup
    filteredList = []

    #search the grid for students with the instrument
    for i in range(len(grid)):

        #if student with instrument found then append it to a new list
        if lName in grid[i][1]:
            filteredList.append(grid[i])
    
    return filteredList



def main():
    ''' This function orchestrates the main behaviour of the program. '''

    #assign label for the csv filename
    filename = './grandstaff.csv'

    #assign csv information to a variable
    grid = readFile(filename)

    #Greet the user and display main menu
    print("\n========================")
    print("|Welcome to Grand Staff|\
        \n========================")

    #main loop
    while True:
        
        #main menu
        user = menu()

        #display records
        if user == '1':
            print("")
            displayTable(grid)
            user = input("\nFilter records by: \
                \n[1] First Name\
                \n[2] Last Name\
                \n[3] Instrument\
                \n[0] Return to main menu\
                \n> ")
            #display by first name
            if user == '1':
                fName = input("What first name? \
                    \n> ").title()
                if len(filterByFName(grid,fName))>0:
                    displayTable(filterByFName(grid,fName))
                else:
                    print(f"\nNo students with the first name '{fName}'.")
            #display by last name
            elif user == '2':
                lName = input("What last name? \
                    \n> ").title()
                if len(filterByLName(grid,lName))>0:
                    displayTable(filterByLName(grid,lName))
                else:
                    print(f"\nNo students with the last name '{lName}'.")
            #display by instrument
            elif user == '3':
                instrument = input("What instrument? \
                    \n> ").title()
                if len(filterByInst(grid,instrument))>0:
                    displayTable(filterByInst(grid,instrument))
                else:
                    print(f"\nNo student with the instrument '{instrument}'.")
            elif user == '0':
                continue
            #display all
            # elif user == '4':
            #     displayTable(grid)
        
        #create student profile
        elif user == '2':
            createStudent(filename)
            grid = readFile(filename)   #update the grid with current info
        
        #modify student credits
        elif user == '3':
            studentCredits(grid)
            while True:
                save = input("Save your changes?: ")
                save = save.upper()
                if save == 'YES' or save == 'Y':
                    print("")
                    saveWork(filename,grid)
                    break
                elif save == 'N' or save == 'NO':
                    break

        #modify student info...
        elif user == '4':
            print("This function is not setup yet...")

        #print help section...
        elif user == '9':
            print("Help section coming soon...")
            
        #quit program
        elif user == '0':
            while True:
                save = input("Save before quitting?: ")
                save = save.upper()
                if save == 'YES' or save == 'Y':
                    saveWork(filename,grid)
                    break
                elif save == 'N' or save == 'NO':
                    print("")
                    break
            exit()
    

main()



''' Fixes:
2. formatting of student info in table when labels are too large
3. student number maybe for students with same name
4. command to return to main menu at any time
5. ability for credits to be floats
6. handle negative credits
7. make it specific to person (name and studio)
'''
