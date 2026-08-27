import math

num1 = int(input("Enter Largest number : "))
num2 = int(input("Enter Smallest number : "))

lcm = abs(num1 * num2) // math.gcd(num1, num2)

print("LCM is : ", lcm)