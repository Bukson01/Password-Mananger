# import the necessary library
from cryptography.fernet import Fernet

# creats a key used to verify the password input
def create_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
create_key()

# returns the key from the .key file
def load_key():
    File = open("key.key","rb")
    key1 = File.read()
    File.close()
    return key1

# prompts owner for master key and also encodes the password
master_pwd = input("Enter your master password: ")
key1 = load_key() + master_pwd.encode()
fer = Fernet(key1)

# appends the password to a file
def add():
    name = input("Username: ")
    pwd = input("Password: ")
    with open("Password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# allows one to view the list of passwords in the file
def view():
    with open("Password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user , passw = data.split("|")
            print("User: ", user , "Password: ", fer.decrypt(passw.encode()).decode())

# promts requesting what action to take given a password
while True:
    mode = input("Would you like to add a new password or view the existing ones?(add/view) or enter q to quit? ").lower()
    if mode == "q":
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode!")
        continue    
