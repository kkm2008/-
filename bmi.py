weight=float(input("몸무게:"))
height=float(input("키:"))


bmi=weight/(height/100)**2


print("BMI:{:.2f}".format(bmi))
