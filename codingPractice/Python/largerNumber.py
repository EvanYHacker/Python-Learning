def find_larger(num1, num2): 
  larger = num2
  smaller = num1
  if (num1 > num2):
    larger = num1
  return larger
 

num1= input("The first number to compare: \n")
num2= input("The second number to compare: \n") 
print("The larger number is ", find_larger(num1, num2))

