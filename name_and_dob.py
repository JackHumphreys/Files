import pickle
data = []
name = input("Please input your name: ")
dob = input("Please input your date of birth: ")
data.append(name)
data.append(dob)
with open("U:\git\Files\database.txt", mode= "wb") as database:
    pickle.dump(data,database)


    
    
