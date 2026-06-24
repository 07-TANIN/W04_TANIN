# dictionary
phone_book = {}
phone_book2 = dict()

# สร้างค่าใน dictionary
student = {
    "name": "Jhon",
    "Gender": "Male",
    "Age": 20,
    "tel": "012-345-6789"
}
#############################
# แก้ไขค่าใน dictionary
# student["Age"] = 30
# student["Gender"] = "Female"
# print(student["Age"])
# print(student["Gender"])
#############################
# การลบค่าใน dictionary
# del student["Age"]
data_pop = student.pop("Age", "ไม่มีข้อมูล")  # ลบค่าใน dictionary และเก็บค่าที่ลบไว้ในตัวแปร remove_value
print(data_pop)  # แสดงค่าที่ลบออกไป

# name_student = student.get("name", "ไม่มีข้อมูล")  # ใช้ get เพื่อดึงค่าใน dictionary
# print(name_student)

# room_number, capacity, equipment, teacher,
class_room = {
    "room_number": "R302",
    "capacity": 30,
    "equipment": ["computer", "projector"," whiteboard"],
    "teacher": {""
    "name": "Mr. Smith",
    "subject": "Math",
    "tel": "012-345-6789"
    }
}
class_room_check = class_room.get("room_number", "ไม่มีข้อมูล")  # ใช้ get เพื่อดึงค่าใน dictionary
print(class_room_check)  # ดึงค่าใน dictionary ซ้อนกัน
