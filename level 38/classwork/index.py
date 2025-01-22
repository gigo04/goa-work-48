#შექმენით ფუნქცია სახელად manual_difference, რომელიც არგუმენტად მიიღებს ორ sets, ფუნქციამ უნდა იმუშაოს იგივენაირად, როგორც ჩაშენებული ფუნქცია .difference


def manual_difference(set1, set2):
    result = set()
    for item in set1:
        if item not in set2:
            result.add(item)
    return result
set1 = (1, 2, 8, 9)
set2 = (1, 2, 4)
print(manual_difference(set1, set2))
