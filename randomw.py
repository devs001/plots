import matplotlib.pyplot as plt
from randomwalk import Random
from
rano=Random(100000)
rano.create_walk()
x_v=rano.x_values
y_v=rano.y_values
plt.figure(figsize=(10, 6))

while True:
    plt.scatter(x_v,y_v,c=y_v,cmap=plt.cm.Blues,edgecolors='none',s=1)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.scatter(x_v[0],y_v[0],c='red',s=50)
    plt.scatter(x_v[-1],y_v[-1],c='green',s=50)

    plt.title('random wlk')
    plt.show()
    again=input("again")
    if again=='no':
        break
    else:
        continue