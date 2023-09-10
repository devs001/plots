from random import choice

class Random():

    def __init__(self,num_walks=5000):
        self.num_walks=num_walks
        self.x_values=[0]
        self.y_values=[0]

    def create_walk(self):
        while len(self.x_values)<self.num_walks:
            numx= self.genrate_choice()
            numy= self.genrate_choice()
            if numx==0 and numy==0:
                continue
            numx=self.x_values[-1]+numx
            numy=self.y_values[-1]+numy
            self.y_values.append(numy)
            self.x_values.append(numx)

    def genrate_choice(self):
        step=choice([1,2,3,4,7,8,9,11,0])
        backorforth=choice([-1,1])
        return step*backorforth


