def numberOfBits(n):
    ones = 0
    zeros = 0
    while(n):
        if(n&1 == 1):
            ones += 1
        else:
            zeros += 1
        n >>= 1
    print("Ones: ", ones, "\nzeros: " , zeros)
    
n = int(input("enter a Number: "))
b = format(n , 'b')
print("The bianary number is: ", b)
numberOfBits(n)