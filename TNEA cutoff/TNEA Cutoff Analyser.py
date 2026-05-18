#This program helps the user to calculate their cutoff and figure out their counselling round
maths=int(input('Enter Your Maths Mark: '))
physics=int(input("Enter Your Physics Mark:"))
chemistry=int(input("Enter Your Chemistry Mark:"))
x=(physics+chemistry)/2 #Physics+chemistry mark
cutoff=x+maths
print("Your TNEA Cutoff :",cutoff)
special=input("Are You Eligible for Ex-servicemen/Sports/Disabled Quota:")#checking for special reservation.
if special.lower() == "yes" and cutoff>=70:#Eliminates the failed ones even if they are eligible for special reservation.
    print('You Are In Special Counselling')
elif cutoff>=179.5:
    print('You Are In Round One Counselling')
elif cutoff>=143 and cutoff<179.5:
    print("You Are In Round Two Counselling")
elif cutoff>=70 and cutoff<143:
    print("You Are In Round Three Counselling")
else:
    print('You Are Not Eligible For Counselling')

 #This part of the program helps the user to find out whether they are eligible for AICTE TFW seat.
income=int(input("Enter Your Income:"))
if income<800000:
    print("You Are Eligible For TFW Seat!!!")
else:
    print('You Are Not Eligible For TFW Seat')
