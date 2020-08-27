#BASIC UP TO GENERATION OF ACCOUNT NUMBER

# import random

# class User():
    

#     def __init__(self, name, age, email, phone):
        
#         self.name = name
#         self.age = age
#         self.email = email
#         self.phone = phone

# class Account(User):


#     def __init__(self, name, age, email, phone):  #INITIALIZE CHILD CLASS

#         super().__init__(name, age, email, phone) #INITIALIZE ATTRIBUTES FROM PARENT CLASS

#         self.balance = 0
#         self.account_no = self.generate_acct_no()

    
#     def generate_acct_no(self):

#         account_num = random.randint(3000000000, 3000009999)

#         return str(account_num)
        


# x = Account("Atha", 23, "inyangete@gmail.com", "08012345678")        

# print(x.account_no)

# ^ WE COMMENTED AND RESTARTED CODE BELOW FOR VERSION CONTROL


import random

class User():
    

    def __init__(self, name, age, email, phone):
        
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

class Account(User):


    def __init__(self, name, age, email, phone):  #INITIALIZE CHILD CLASS

        super().__init__(name, age, email, phone) #INITIALIZE ATTRIBUTES FROM PARENT CLASS

        self.balance = 0
        self.account_no = self.generate_acct_no()

    
    def generate_acct_no(self):

        account_num = random.randint(3000000000, 3000009999)

        return str(account_num)
        
    def deposit(self, amount, comment = ""):

        self.balance += amount #ADD DEPOSIT VALUE TO BALANCE
        self.store_history("credit", amount, comment)

        print(f"Weldone {self.name}, your deposit of ₦{amount} was successful, your new balance is ₦{self.balance}.")


    def withdraw(self, amount, comment = ""):

        self.balance -= amount #SUBTRACT WITHDRAWAL VALUE FROM BALANCE
        self.store_history("debit", amount, comment)

        print(f"Weldone {self.name}, your withdrawal of ₦{amount} was successful, your new balance is ₦{self.balance}.")


    def transfer(self, amount, recipient, comment = ""):

        self.balance -= amount  #REMOVE TRANSFER AMOUNT FROM SENDER'S BALANCE
        recipient.balance += amount #ADD TRANSFER AMOUNT TO RECIPIENT BALANCE

        self.store_history("transfer", amount, comment, recipient.name)

        print(f"Congrats {self.name}, your transfer of ₦{amount} to {recipient.name} was successful, your new balance is ₦{self.balance}.")
    
    def store_history(self, type, amount, comment, receiver = "Same as Sender"):
        file = open("financial statement.csv", "a")
        file.write(f"{type}, {self.name}, {amount}, {comment}, {receiver}\n")

        print(type, amount, comment, receiver)




atha = Account("Atha", 23, "inyangete@gmail.com", "08012345678")        

print(atha.account_no)

atha.deposit(20000)

atha.withdraw(10000)

bolu = Account("Bolu", 33,"bolu@gmail.com", "08098765432")  

atha.transfer(2000, bolu, "flexing")