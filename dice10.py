from doll import Die
import pygal
def genrate_result(die_object):
    lis=[]
    for i in range(100000):
        lis.append(die_object.roll_on())
    return lis
dieten=Die(10)
dien=Die()
die_lis_ten=[]
die_lis_n=[]
sum_of_dies=[]
die_lis_ten=genrate_result(dieten)
die_lis_n=genrate_result(dien)
occuring_num=[]
for i in range(100000):
    occuring_num.append(die_lis_ten[i]*die_lis_n[i])
for i in range(1,60):
    sum=occuring_num.count(i)
    sum_of_dies.append(sum)
webchart=pygal.Bar()
webchart.x_labels=[i for i in range(1,60)]
webchart.x_title='xxxx title'
webchart.y_title="yyyyyyyy title"
webchart.add('d10-6',sum_of_dies)
webchart.render_to_file('files_for die1014.svg',)