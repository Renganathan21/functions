# functions
def bank(acc_num):
    bal={'RENGA0720':10000,'SATISH0720':5000,'MILAN1432':2500,'RICHARD1234':2000,'RAHUL4567':1000}
    for i in bal.keys():
        if(acc_num == i):
            b = bal[i]
    return b
def getdata():
    print(" Enter :\n\t1 - WITHDRAW \n\t2 - DEPOSIT \n\t3 -BALANCE  \n\t4 - EXIT")
    n=int(input("Enter your choice : "))
    return n
def withdraw(b,amount):
    if (b <=2000):
        print(b)
        print("\t\toops..! your balance amount is below minimum balnce so please deposit some amount to your accont ")
        print("\t\t\t\t-----------thankyou------------")
    elif ((b-amount)<0):
        print("your amount exceeds your blance amount please have a check over it ")
        print("\t\t\t\t-----------thankyou------------")
    elif ((b-amount)<2000):
        b-=amount
        print("please be aware that your balnce went below minimum balance ")
    else:
        b-=amount
    return b


def deposit(b,d):
    b+=d
    print("your amount has been successfully deposited ")
    print(d)
    return b,d


def display (n,name,acc_num,code,branch,b,amount,d):
    print("\n\t\t NAME           : ",name.upper())
    print("\n\t\t ACCOUNT NUMBER : ",acc_num)
    print("\n\t\t IFSC CODE      : ",code)
    print("\n\t\t BRANCH         : ",branch.upper())
    if(n==1):
        print("\n\t\t\t your withdraw amount : ",amount)
        print("\n\t\t\t your current balance in your account : ",b)
        print("*"*100,"\n")
    elif(n==2):
        print("\n\t\t\t your deposit amount : ",d)
        print("\n\t\t\t your current balance in your account : ",b)
        print("*"*100,"\n")
    else:
        print("\n\t\t\t your current balance in your account : ",b)
        print("*"*100,"\n")
    
def detail():
    n=True
    a=0

    while(n):
        if(a==0):
            name=input("Enter your name  : ")
            acc_num=input("Enter your account num :")
            code=int(input("Enter your ifc code : "))
            branch=input("Enter your branch name : ")
            a=1
            b=bank(acc_num)


        n=getdata()

        if(n==1):
            print("*"*100,"\n")
            print("\n\n\t\t------WITHRAW RECEIPT------")
            amount=float(input("Enter your withdraw amount : "))
            b=withdraw(b,amount)
            d=0
            display(n,name,acc_num,code,branch,b,amount,d)
        elif(n==2):
            print("*"*100,"\n")
            print("\n\n\t\t------DEPOSIT RECEIPT------")
            amount=0
            d=int(input("Enter your deposit amount : "))
            b,d=deposit(b,d)
            display(n,name,acc_num,code,branch,b,amount,d)
        elif(n==3):
            print("*"*100,"\n")
            print("\n\n\t\t------BALANCE RECEIPT------")
            amount=0
            d=0
            display(n,name,acc_num,code,branch,b,amount,d)
        else:
            n=False

    print("\t\t\t------THANKYOU FOR APPROCHING AND FETCHING DETAILS ---------")

try:
    detail()
except NameError :
    print("\n\n*******please check your account number and enter a valid one********** ")
    detail()
