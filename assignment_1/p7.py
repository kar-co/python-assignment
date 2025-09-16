from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
users = {
    "admin" : cipher.encrypt(b"12345"),
    "varun" : cipher.encrypt(b"67890")
}

username = input("Enter username: ")
if username not in users:
    print("Invalid Username")
else:
    password = input("Enter password: ")
    stored_password = cipher.decrypt(users[username]).decode()
    if(password == stored_password):
        print("Login Successful!")
    else:
        print("Invalid Password")