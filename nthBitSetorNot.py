def setorNot(number, n):
  if number & (1 << (n-1)):
    print("SET")
  else:
    print("NOT SET")

num = int(input("Enter a number: "))
n = int(input("enter a number: "))
b = format(num, 'b')
print(b)
setorNot(num, n)