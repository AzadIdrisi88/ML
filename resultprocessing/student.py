class student:
    def __init__(self,rollno=None,name=None) -> None:
        if rollno is None:
            self.rollno=int(input("Enter Roll no. = "))
        else:
            self.rollno=rollno
        if name is None:
            self.name= input("Enter Your Name = ")
        else:
            self.name=name
    def __str__(self) -> str:
        return "name={0},rollno={1}".format(self.name,self.rollno)
    
    
