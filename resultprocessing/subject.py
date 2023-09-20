class subject:
    def __init__(self,subject=None,maxmarks=None,minmarks=None,obtainmarks=None) -> None:
        if subject is None:
            self.subject=input(" Enter Subject = ")
        else:
            self.subject=subject
        if maxmarks is None:
            self.maxmarks=int(input('Maxmarks = ')) 
        else:
            self.maxmarks=maxmarks
        if minmarks is None:
            self.minmark=int(input('Minmarks = '))
        else:  
            self.minmark=minmarks
        if obtainmarks is None:
            self.obtainmarks=int(input('Obtainmarks = ')) 
        else: 
            self.obtainmarks=obtainmarks
    def __str__(self) -> str:
        return "subject={0}, maxmarks={1},minmarks={2},obtainmarks={3}".format(self.subject,self.maxmarks,self.minmark,self.obtainmarks)