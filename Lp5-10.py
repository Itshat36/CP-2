num1 = int(input("Enter number 1:"))
num2 = int(input("Enter a second number:"))

while (num2 > 0):
  temp = num1 % num2;
  num1 = num2;
  num2 = temp;
  print("GCD:",num2)
  