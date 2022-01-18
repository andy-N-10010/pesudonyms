import sys, random

def generateName():
    firstName = ["Billy","Bob", "Baby Oil", "Andy","Andy Jr", "Serenity", "Eyasu Jr", "Tommy"]

    lastName = ["Bigmeat", "Hooperbag", "Jenkins", "Brown", "Swith", "Rugrats"]

    randomNum = random.randint(0,len(firstName)-1)
    randomNum2 = random.randint(0, len(lastName)-1)

    chosenFirstName = ""

    for i in range(len(firstName)):
        if randomNum == i:
            chosenFirstName = firstName[i]

    chosenLastName = ""

    for j in range(len(lastName)):
        if randomNum2 == j:
            chosenLastName = lastName[j]
            
    genName = chosenFirstName + " " + chosenLastName
     
    return genName
    

#print(choosenLastName)

if __name__ == "__main__":
    
    print("Welcome to pseudonyms!\nCome up with custom names on the fly.")
    
    validation = False
    
    while validation == False:
        
        userInput = input("Enter start to begin: ")
        if userInput == "start":
            
            validation = True
            
            newName = generateName()
            
            print("\n"+newName +"\n")
            
        else:
            print("\nIncorrect input. Try again.\n")
        
    validation2 = False
    
    while validation2 == False:
        
        userInput2 = input("Keep going? y/n: ")
        if userInput2 == "y":
            newName = generateName()
            
            print("\n"+newName + "\n")
            
        elif userInput2 == "n":
            
            validation2 = True
            
            print("\nGoodbye.")
            
        else:
            print("Incorrect input. Try again.")
            
