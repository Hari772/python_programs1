# assigning a grade to a student
#student name
#student roll number
# total subjects ---- 6
#telugu
#english
#social
#math
#science
#hindi
# average?
# conditional statements
# 90-100 ---> A+
# 80-89  ---> A
# 70-79  ---> B
# 60-69 ---> C
# 50-59 ---> D
# 40-49 ---> E
# below 40 ---> Fail
name=input("Enter the name: ")
roll_no=input("Enter the roll no: ")
t=int(input("total subjects:"))
telugu=eval(input("Enter telugu marks:"))
hindi=eval(input("Entre hindi marks:"))
english=eval(input("Enter english marks:"))
science=eval(input("Enter science marks:"))
social=eval(input("Enter social marks:"))
math=eval(input("Enter math marks: "))
average=(telugu+hindi+english+science+social+math)/6
print(f"the average marks of {name} is {average}")

if average>=90 and average<=100:
    print("Grade ---->  A+")
elif average>=80 and average<=89:
    print(" Grade  ----->  A")
elif average>=70 and average<=79:
    print("Grade -----> B")

elif average>=60 and average<=69:
    print("Grade -----> C")
elif average>=50 and average<=59:
    print("Grade ----->  D")
elif average>=40 and average<=49:
    print("Grade ----> E")
elif average>100 or average<0:
    print("Invalid")
else:
    pass
