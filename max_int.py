#1. while input is equal to or larger than 0 check input
#2. if input is larger than the current largest integer replace it with current input integer
#3. ask for input again
#4. check until input is negative and print the largest integer
num_int = int(input("Input a number: "))
max_int=0
while num_int >= 0:
    if num_int>max_int:
        max_int=num_int
    num_int=int(input("Input a number: "))
if num_int<0:
    print("The maximum is", max_int) 
