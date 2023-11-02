from movies import Movies

movies = Movies('./movies.txt')


input = scan("Please enter an input\nsn: search by name\nsc: search by cast\nlist: print entire list")
while input.lower != "q":
    
    if(input == "sn"):

    elif(input == "sc"):

    elif(input == "list"):
        list()

    input = scan("Please enter an input")

def list():
    for i in range(len(movies._movies)):
        print(movies._movies[i]['name'])




