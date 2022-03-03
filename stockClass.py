#Nicholas Kantarellis,Dongmin Li
#stockClass
#initial class to put all our stocks into
class Stock:
    #Define stock by name expected return, risk, standard deviation,calculate best return
    def __init__(self,name,ER,risk,std,U):
        self.name=name
        self.ER=ER
        self.risk=risk
        self.std=std
        self.U=0.0

    
