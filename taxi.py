"""write a program that arranges taxis in how they are supposed to move in and out.
      PSEUDO CODE
input the taxi plate, the number and the type .
arrange the taxis according to their registration number.
output a list if the arrangement of the taxis according to their order of registration."""
class taxi:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def __repr__(self):
        return str((self.a, self.b,self.c,self.d))
    
taxis = [taxi("registrationNum",23,"taxiPlate","837AD"),
         taxi("registrationNum",32,"taxiPlate","43598AD"),
         taxi("registrationNum",2,"taxiPlate","0309AD"),
         taxi("registrationNum",24,"taxiPlate","9747AD")] 
print(sorted(taxis, key=lambda x:x.b))