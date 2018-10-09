#就那个银行系统吧，看看能不能实现
#没有对象,纯数组实现，话说python里面素有东西都是对象
bankUsers=[]
#是一个类
class BankUser:
    def __init__(self,bankid,name,balance):
        self.bankid = bankid
        self.name = name
        self.balance = balance
    def putOut(self):
        print(self.name)
        print(self.bankid)
        print(self.balance)

name = input("请输入名字:")
bankid = input("请输入年龄:")
balance = input("请输入余额:")
user = BankUser(bankid,name,balance)
