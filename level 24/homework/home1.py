#მეორე

def my_join(items, seperator):
    result = ""
    for i in range(len(items)):
        result += items(i)
        if i != len(items)-1:
            result += seperator
            return result
