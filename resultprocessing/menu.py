class menu:
    def __init__(self,search,exit,add) -> None:
        self.search=search
        self.exit=exit
        self.add=add
    def __str__(self) -> str:
         return "search={0},exit={1},add={2}".format(self.search,self.exit,self.add)