def password():
    passwordVar = input("Enter Password \n")

    if passwordVar == "Knights19":
        return "Access Granted"
    else:
        return "Access Denied"

print(password())