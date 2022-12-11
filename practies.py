class Account:
    def __init__ (self):
        self.First_name= []
        self.Last_name =[]
        self.gender =[]
        self.address = []
    def push(self,value):
        self.First_name.append(value)
list = Account()

list.push("Yabsira")
list.push("Ashenafi")
list.push("male")
list.push("megenagne")

print(list.First_name)
