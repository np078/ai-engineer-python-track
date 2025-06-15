def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b ==0:
        return "Error!, Division by Zero is not possible"
    return a/b

print("Welcome to CLI based Calculator")
print("Operations: + - * /")
history = []

while True:    # It will run loop forever untill manually broken
    
  try:
    num1=float(input("Enter the first number: "))
  except ValueError:
     print("Please Enter a valid Input")
     continue                                    # This continue statement will skips the rest of the loop and start over, if an invalid input is entered
  op=input(("Enter the opeator(+, -, *, /): "))
  num2=float(input("Enter the second number: "))

  if op=='+':
        result =  add(num1,num2)

  elif op=='-':
        result =  subtract(num1,num2)

  elif op=='*':
        result =  multiply(num1,num2)

  elif op=='/':
        result =  divide(num1,num2)

  else:
        print("Invalid Operator")
        continue

  history.append(f"{num1} {op} {num2} = {result}")
  print("Result: ", result)

  cont = input("Do you want to continue? (y/n): ")
  if cont!= 'y':
        print("Thank you for using CLI calculator")
        print("Calculation History: ")
        for h in history:
             print(h)
        break
