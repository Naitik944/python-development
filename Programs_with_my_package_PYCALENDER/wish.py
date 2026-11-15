from pycalender import gdw

name = input("Enter your name: ")
input("I HAVE A SURPRISE FOR YOU! PRESS ENTER TO CONTINUE: ")
year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day_of_month = int(input("Enter your birth date: "))

try:
    day = gdw(year, month, day_of_month)
except ValueError as error:
    print(f"Invalid birth date: {error}")
    raise SystemExit(1)

print("ARE YOU READY FOR YOUR SURPRISE? ")
input("Press enter to continue: ")
print("WHAT IF I KNOW THE EXACT DAY YOU WERE BORN?")
input("Press enter to continue: ")
print("YOU WERE BORN ON ", day)