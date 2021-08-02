import random
z=random.randint(1,80)
x=int(input('가격:'))
y=x*(z/100)
print(z,"%","할인 당첨")
print("가격:",int((x-y)//100*100)+(x-y)//100*100/10)
