def math_position(x, math_position):
    
    arr = []
    while x > 0:
        sum = x % math_position
        arr.append(sum)
        x = x // math_position
    return arr[::-1]
print(bin(math_position(9)))
print(bin(math_position(10)))
decimal = sum(int(digit) * (2 ** i) for i, digit in enumerate(reversed(binary_str)))