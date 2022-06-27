class BankAccount(object):
    
    def __init__(self, name, money, address):
        self.name = name
        self.__money = money
        self.address = address
    
    def getMoney(self):
        return self.__money
    
    def setMoney(self, amount):
        self.__money = amount
        # private
    def __increase(self):
        self.__money = self.__money + 500
#
p1 = BankAccount("messi", 1000, "Barcelona")
p2 = BankAccount("neymar", 2000, "Paris")

print("get method : ",p1.getMoney())

p1.setMoney(5000)
print("after set method : ",p1.getMoney())

# p1.__increase()
# print("After raise : ",p1.getMoney())