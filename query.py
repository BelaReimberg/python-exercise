from movies import Movies

movies = Movies('./movies.txt')

def list():
    for i in range(len(movies._movies)):
        print(movies._movies[i]['name'])

def sn(substring):
    for i in range(len(movies._movies)):
        if(substring.lower() in movies._movies[i]['name'].lower()):
            print(movies._movies[i]['name'])

def sc(substring):
    for i in range(len(movies._movies)):
        matchList=[]
        for j in range(len(movies._movies[i]['cast'])): # go through cast array
 
            if(substring.lower() in movies._movies[i]['cast'][j].lower()):
                matchList.append(movies._movies[i]['cast'][j])
                
        if(len(matchList) != 0):
            print(movies._movies[i]['name'])
            print(matchList)




userInput = input("Please enter an input\nsn: search by name\nsc: search by cast\nlist: print entire list\nq:quit\n").lower()
while userInput != "q":
    
    if(userInput == "sn"):
        inputName = input("please enter a string to search by name:\n")
        sn(inputName)

    elif(userInput == "sc"):
        inputName = input("please enter a string to search by cast:\n")
        sc(inputName)

    elif(userInput == "list"):
        list()

    userInput = input("Please enter an input\nsn: search by name\nsc: search by cast\nlist: print entire list\nq:quit\n").lower()





