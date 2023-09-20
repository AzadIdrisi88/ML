class Myclass:
    x=8
p1=Myclass()
print('P1',p1.x)

class person:
  def __init__(self,name,age,city):
    self.name=name
    self.age=age
    self.city=city
p2=person('Ankit Mohan',25,'varanasi')
print('The name of student:',p2.name)
print('Age:',p2.age)
print('City:',p2.city)

class student:
   def __init__(currentobj,name,stream,age) :
      currentobj.name=name
      currentobj.stream=stream
      currentobj.age=age
    
   def myfunc(xyz):
        print('Hello, My name is '+ xyz.name)
        print('And My Stream is '+ xyz.stream)
        print('My Age is '+ str(xyz.age))


p2=student('Ashhad Azad','science',21) 
# p2.age=25  
p2.myfunc()
del p2.age
p2.myfunc()
class train:
   pass
   