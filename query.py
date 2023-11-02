from movies import Movies

movies = Movies('./movies.txt')

def list():
    for i in range(len(movies._movies)):
        print(movies._movies[i]['name'])

def sn(substring):
    for i in range(len(movies._movies)):
        if(substring.lower() in movies._movies[i]['name'].lower()):
            print(movies._movies[i]['name'])

userInput = input("Please enter an input\nsn: search by name\nsc: search by cast\nlist: print entire list\n").lower()
while userInput != "q":
    
    if(userInput == "sn"):
        inputName = input("please enter a string to search by name:\n")
        sn(inputName)

    elif(userInput == "sc"):
        inputName = input("please enter a string to search by name:\n")

    elif(userInput == "list"):
        list()

    userInput = input("Please enter an input\nsn: search by name\nsc: search by cast\nlist: print entire list\n").lower()





