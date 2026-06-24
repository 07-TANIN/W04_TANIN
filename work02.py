[]
f = {
    "a" : "dsfdsf"
}
t = {"f","d","7"}

# set
music_club = {"Adele", "Beyonce", "Coldplay", "Drake"}
color = {"Red", "Blue", "Green", "Yellow",} 
friut = {"Apple", "Banana", "Cherry", "Date","Red"}
# print("รายชื่อ",music_club,"\n","สี",color,"\n","ผลไม้",friut)
# print(f"รายชื่อ: {music_club}\nสี: {color}\nผลไม้: {friut}")

# Union
all_members = music_club | color | friut
# print(f"รายชื่อ: {all_members}")

# Intersection (&)
color_friut = color & friut
# print(f"รายชื่อ: {color_friut}")

# complement (-)
dif_color_friut = color - friut
# print(f"รายชื่อ: {dif_color_friut}")

# symmetric difference (^)
sym_color_friut = color ^ friut
# print(f"รายชื่อ: {sym_color_friut}")

# การตรวจสอบสมาชิกใน set
set_chack = {"Apple","Banana"}
if set_chack.issubset(color):
    print("มี")
else:
    print("ไม่มี")