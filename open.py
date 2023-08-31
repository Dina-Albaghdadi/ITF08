with open("itf8.txt","a") as file:
    name = input("Enter your name:")
    age = input("Enter your age:")
    date_of_birth = input("Enter your Birthdate according to this format(DD-MM-YYYY):")
    file.write(name+"\t")
    file.write(age +"\t")
    file.write(date_of_birth+"\n")
    file.close()