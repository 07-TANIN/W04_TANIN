Username = "admin"
Password = "1234"

input_username = input("กรุณากรอก Username: ")
input_password = input("กรุณากรอก Password: ")

if input_username == Username and input_password == Password:
    print("ยินดีต้อนรับเข้าสู่ระบบ")
else:
    print("เข้าสู่ระบบล้มเหลว! Username หรือ Password ไม่ถูกต้อง")