def	calculate(num1, operator, num2):
	if operator == "+":
		result = num1 + num2
	if operator == "-":
		result = num1 - num2
	if operator == "*":
		result = num1 * num2
	if operator == "/":
		result = num1 / num2
	return result

print(calculate(10,"+",10))
print(calculate(10,"-",10))
print(calculate(10,"*",10))
print(calculate(10,"/",10))