
n = int(input("Enter the length of the sequence: ")) 
first_int=1
second_int=2
third_int=3
equation=0
#first print the first 3 integer
for i in range (n+1):
    if i==0:
        print(1)
    if i==1:
        print(2)
    if i==3:
        print(3)
#when i number goes above 3 execute algorithm where the last 3 numbers are added together to print the new number
    if i>3:
        equation=first_int+second_int+third_int
        first_int=second_int
        second_int=third_int
        third_int=equation
        print (equation)