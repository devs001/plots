import matplotlib.pyplot as plt
import random

lisx=[range(-100,1001)]
lisy=[i*i for i in range(-100,1001)]
# s for put list and linewidht for thinkness of line

plt.scatter(lisx,lisy,s=30,c=lisy,cmap=plt.cm.Greens,edgecolors='none')

#title font self explintory

plt.title("here we start",fontsize=22)

plt.xlabel("fun",fontsize=23)
plt.ylabel("tun",fontsize=33)
plt.tick_params(axis="both",labelsize=11)
plt.axis([0,1100,0,1100000])

plt.savefig('sav.png',bbox_inches='tight')
plt.show()
