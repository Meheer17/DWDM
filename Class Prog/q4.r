num1=as.integer(readline(prompt = "enter the first number:"))
num2=as.integer(readline(prompt = "enter the second number:"))
if (num2 == 0) {
  print("Error: Division by zero is not allowed.")
} else {
  num3=num1/num2
  print(num3)
}