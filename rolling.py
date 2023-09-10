from doll import Dien
import pygal
die1=Dien()
die2=Dien()
sum_of_result = []

result=[]


for i in range(1000):
    i = die1.roll_on()
    j = die2.roll_on()
    su=i+j
    result.append(su)

for i in range(1, 2**(die1.choice_num)+1):
    sum=result.count(i)
    sum_of_result.append(sum)
print(sum_of_result)

hist=pygal.Bar()

hist.title="hostrol"
hist.x_labels=[1,2,3,4,5,6,7,8,9,10,11,12]
hist.y_title="y title"
hist.x_title='t title'
hist.add("d7",sum_of_result)
hist.render_to_file('die_diec2.svg')

