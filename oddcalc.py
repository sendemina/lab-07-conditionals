firstnumber = input("Give me a number, any number... ")
secondnumber = input("Cool, now another number... ")
operation = input("Now choose an operation (mul, div, or mod) ")
if operation == "mul":
  print(float(firstnumber) * float(secondnumber))
elif operation == "div":
  print(float(firstnumber) / float(secondnumber))
elif operation == "mod":
  print(float(firstnumber) % float(secondnumber))
else:
  print("Invalid Operation!")
