class BankAccount:
    def __init__(self):
        self.accountno=int(input("Enter Account No"))
        self.customername=input("Enter Name")
        self.balance=int(input("Enter Balance"))
    def __str__(self):
       return"Account Number={0} Customer Name={1} Account Balance={2}".format(self.accountno,self.customername,self.balance)
    def deposit(self):
        amount=int(input("Enter Amount to deposit"))
        self.balance+=amount
    def withdraw(self):
        amount=int(input("Enter Amount to withdraw"))
        if amount<=0:
            print ("Invalid Amount")
            return
        if(amount>self.balance):
            print("Insufficient amount")
            return
        self.balance-=amount
        
accounts={}    
while(True):
    
    print("0-Exit,1-Create,2-Deposit,3-Withdraw,4-View")
    option=int(input("option="))
    if option==0:
        break
    if option==1:
        account=BankAccount()
        accounts[account.accountno]=account
    if(option==2):
        acccountno=int(input("account no="))
        account=accounts.get(acccountno)
        if account!=None:
            account.deposit()
            print(account)
        else:
            print("Account Not Found")
            
    if(option==3):
        acccountno=int(input("account no="))
        account=accounts.get(acccountno)
        if account!=None:
            account.withdraw()
            print(account)
        else:
            print("Account Not Found")
    if(option==4):
        print(accounts)
