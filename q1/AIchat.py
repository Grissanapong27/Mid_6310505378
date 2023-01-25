
def showSubjectName():
	print("Artificial intelligence System for Robots")
	
def showStudentYear():
	id = input("your ID:")
	id = id/10000000
	year = 66-id
	print(year)
	
def calculator():
	syn = input()
	result = 0
	num1 = int(input("num1 ="))
	num2 = int(input("num2 ="))
	if(syn == "+"):
		result = num1 + num2
	if(syn == "-"):
		result = num1 - num2
	print(result)
	
	
main()
	showSubjectName()
	showStudentYear()
