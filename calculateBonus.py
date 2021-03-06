yow=int(input("Enter yow: "))
salary =int(input("Enter Salary:"))


if((yow>=0) and (yow<3)):
    bonus =(salary*3)/100
    salary=bonus+salary
elif((yow>=3) and (yow<5)):
    bonus =(salary*3)/100
    salary=bonus+salary
elif(yow>=5):
    bonus =(salary*10)/100
    salary=bonus+salary
else:
    print("Invalid Input")

print(bonus)
print(salary)
