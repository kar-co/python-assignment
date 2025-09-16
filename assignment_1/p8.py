import hashlib 
username = "Admin" 
password_hash = hashlib.sha256("123".encode()).hexdigest() 
uname = input("Enter Username: ") 
pwd = input("Enter Password: ") 
pwd_hash = hashlib.sha256(pwd.encode()).hexdigest() 
if uname == username and pwd_hash == password_hash: 
print("Login successful!") 
else: 
print("Invalid Username or Password")