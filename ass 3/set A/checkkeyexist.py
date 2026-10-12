user_info={
    "username":"johndoe",
    "email":"jondoe@gmail.com",
    "age":30
}
key_to_check="email"
if key_to_check in user_info:
    print(f"the key exists in dictionary")
else:
    print("key dosen't exist")