import base64 
original_string = "Hello$World" 
string_bytes = original_string.encode("utf-8") 
base64_bytes = base64.b64encode(string_bytes) 
base64_string = base64_bytes.decode("utf-8") 
print("Original String:", original_string) 
print("Base64 Encoded:", base64_string) 
