print("WELCOME;")
print("This program will calculate your final grade based on your scores.")
print("###########################################################################")
diag=input("Please enter any key to continue: ")
sub=str(input("Please enter your subject: "))
num1=float(input("Please enter your  score(out of 100): "))
if num1 > 100:
    print("Please enter a valid score out of 100")
else:
    print("Your scored marks in " + sub + " is: " + str(num1))
    if num1 >= 90:
        print("Your grade is A as per your scored marks in " + sub)
    elif num1 >= 80:
        print("Your grade is B as per your scored marks in " + sub)
    elif num1 >= 70:
        print("Your grade is C as per your scored marks in " + sub)
    elif num1 >= 60:
        print("Your grade is D as per your scored marks in " + sub)
    else:
        print("Your grade is F as per your scored marks in " + sub)