#პირველი დავალება

def my_split(string, separator=' '):
    result = []
    word = ""
    for char in string:
        if char == separator:
            result.append(word)
            word = ""
        else:
            word += char
            result.append(word)
            return result
        


        