import matplotlib.pyplot as plt
from doll import Die
import pygal
d61=Die()
d62=Die()
d63=Die()
def genrate_result(die_object):
    lis=[]
    for i in range(100000):
        lis.append(die_object.roll_on())
    return lis
d61_lis=genrate_result(d61)
d62_lis=genrate_result(d62)
d63_lis=genrate_result(d63)
occured_in_lis=[]
sum_lis=[]
for i in range(100000):
    ouccured_num=d61_lis[i]+d62_lis[i]+d63_lis[i]
    occured_in_lis.append(ouccured_num)
print(occured_in_lis)
for i in range(3,19):
    sum=occured_in_lis.count(i)
    sum_lis.append(sum)
plt.scatter([i for i in range(3,19)],sum_lis,c=sum_lis,cmap=plt.cm.Blues)
plt.xlabel("x part")
webchar=pygal.Bar()
webchar.x_labels= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18]
webchar.x_title='sum of the diec rolled result'
webchar.y_title='occuring time of a number'
webchar.add('d6+d10',sum_lis)
webchar.render_to_file('svrsvar0023.svg')
plt.show()