'''Temperature of a city in Fahrenheit degrees is input through the keyboard
 .Write a program to convert this tempetature into Centigrade degrees'''
while True:
 Fahren=float(input("Enter degree in Fahrenheit degrees(°F):"))
 Centi=(Fahren-32)*1.8
 print("Degrees in Centigrade is",Centi,"°C")
 print("Degrees in Fahrenheit is",Fahren,"°F")