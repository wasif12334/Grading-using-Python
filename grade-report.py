name = input("Enter Your Name: ")
regID = int(input("Enter Your ID: "))
sub1 =  int(input("Enter Math's maks:(MAX-Value = 35 ) "))
sub2 =  int(input("Enter English's maks: (MAX-Value = 35 )"))
sub3 =  int(input("Enter Urdu's maks: (MAX-Value = 35 )"))
grade = " "
totalmark = sub1 + sub2 + sub3 
if totalmark >= 80:
    grade = " A+"
elif totalmark >= 70 and totalmark <= 80:
    grade = " A"
elif totalmark >= 60 and totalmark <= 70:
    grade = " B"
elif totalmark >= 50 and totalmark <= 60:
    grade = " C"
elif totalmark >= 40 and totalmark <= 50:
    grade = " D"

print("\nT\t\t\t\t------REPORT-------\n")
print("\nName :" ,name)
print("\nID :" ,regID)
print("\nGrade :" ,grade)
