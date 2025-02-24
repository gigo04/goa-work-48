#1
for i in range(1, 50, 2):
    print(i, end=" ")

print()  
i = 1
while i < 50:
    print(i, end=" ")
    i += 2



#2
size = 5
for i in range(size):
    print("*" * size)

print()


i = 0
while i < size:
    print("*" * size)
    i += 1



#3
width = 8
height = 4
for i in range(height):
    print("*" * width)

print()

i = 0
while i < height:
    print("*" * width)
    i += 1

#4
print("რეგისტრაციის ფორმა")

while True:
    username = input("შეიყვანეთ თქვენი სახელი: ")
    email = input("შეიყვანეთ თქვენი ელ.ფოსტა: ")
    password = input("შეიყვანეთ პაროლი: ")

    if username and email and password:
        print("✅ რეგისტრაცია წარმატებულია! ✅")
        break
    else:
        print("⚠ გთხოვთ, შეავსოთ ყველა ველი! ⚠")

