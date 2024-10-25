def find_rightmost_set_bit(n):
    if n == 0:
        return -1

    position = 1
    while (n & 1) == 0:
        n = n >> 1
        position += 1

    return position

number = int(input("Enter a number: "))

position = find_rightmost_set_bit(number)

if position == -1:
    print("No set bit found.")
else:
    print(f"Position of the first set bit: {position}")
