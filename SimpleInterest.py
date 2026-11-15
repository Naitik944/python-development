'''Calculate Simple Interest for a set of value representing
principal,number of years and rate of interest.
'''
#Principal(P),Number of years(N),Rate of interest(R)
while True :
 print("Simple Interest➡︎")
 print("NOTE:Don't write any unit like years,%,₹,etc")
 P=int(input("Enter your principal amount(Like ₹1000):₹"))
 N=float(input("Enter number of years(Ex.3 for 3years) :"))
 R=float(input("Enter the rate of interest (Like 8.5)  :"))
 Simple=(P*N*R)/100
 Total=P+Simple
 print("The simple interest is,₹",Simple)
 print("Total payable amount is ,₹",Total)
 print("#@"*10)