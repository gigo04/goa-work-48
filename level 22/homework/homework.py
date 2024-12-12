list_of_names = ["დავით", "ანა", "გიორგი", "დავით", "ნინო", "დავით", "გიორგი"]


target_name = "დავით"
count = 0
for name in list_of_names:
    if name == target_name:
        count += 1

print(f"სახელი '{target_name}' მეორდება {count} ჯერ სიაში.")


  