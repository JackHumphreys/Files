
name = input("Please input your name: ")
dob = input("Please input your date of birth: ")
with open(r"\Users\Jumphreys\Desktop\database.txt", mode= "wb") as database:
    database.write(name.encode("utf-8"))
    database.write(dob.encode("utf-8"))

    
    
