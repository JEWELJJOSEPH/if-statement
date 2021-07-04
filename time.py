''' To check weather its
A)" Good morning" if the time is less than 1200
B)"Good afternoon" if the time is >=1200.
C)"Good evening if time is > 1600 But <=1900.
D)"Good night" '''
time=int(input("Enter the time?:"))
if time < 1200:
    print("Good morning")
elif time <=1600 :
    print("Good afternoon")
elif time <= 1900 :
    print("Good evening")
else :
    print("Good night")
