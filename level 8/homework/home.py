age = int(input("შეიყვანეთ თქვენი ასაკი: "))

if 13 <= age < 19:
    print("თქვენ თინეიჯერი ხართ!")
else:
    print("თქვენ არ ხართ თინეიჯერი.")


score = int(input("ნუგზარ, შეიყვანე შენი საკონტროლო ნიშანი (1-10): "))

is_A = score >= 9
is_B = 8 <= score < 9
is_C = 7 <= score < 8
is_D = 6 <= score < 7
is_F = score < 6

print("is_A:", is_A)
print("is_B:", is_B)
print("is_C:", is_C)
print("is_D:", is_D)
print("is_F:", is_F)



true_var = True
false_var = False

print("AND ოპერატორი:")
print("True AND True:", true_var and true_var)
print("True AND False:", true_var and false_var)
print("False AND False:", false_var and false_var)

print("\nOR ოპერატორი:")
print("True OR True:", true_var or true_var)
print("True OR False:", true_var or false_var)
print("False OR False:", false_var or false_var)

print("\nNOT ოპერატორი:")
print("NOT True:", not true_var)
print("NOT False:", not false_var)




num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

print(f"{num1} == {num2}:", num1 == num2)
print(f"{num1} < {num2}:", num1 < num2)
print(f"{num1} > {num2}:", num1 > num2)
print(f"{num1} <= {num2}:", num1 <= num2)
print(f"{num1} >= {num2}:", num1 >= num2)
print(f"{num1} != {num2}:", num1 != num2)

