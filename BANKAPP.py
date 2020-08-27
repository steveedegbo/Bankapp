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
        
    def deposit(self, amount, comment = "no comment", source = False):

        transaction_label = "credit"

        if source:
            transaction_type = "transfer"
            source = source.name
        else:
            transaction_type = "deposit"
            source = self.name

        self.balance += amount #ADD DEPOSIT VALUE TO BALANCE
        self.store_history(transaction_type, transaction_label, amount, self.name, comment, source)

        print(f"Weldone {self.name}, your deposit of ₦{amount} was successful, your new balance is ₦{self.balance}.")


    def withdraw(self, amount, comment = "no comment", collector = False):

        transaction_label = "debit"

        if collector:
            transaction_type = "transfer"
            collector = collector.name
        else:
            transaction_type = "withdrawal"
            collector = self.name

        self.balance -= amount #SUBTRACT WITHDRAWAL VALUE FROM BALANCE
        self.store_history(transaction_type, transaction_label, amount, self.name, comment, collector)

        print(f"Weldone {self.name}, your withdrawal of ₦{amount} was successful, your new balance is ₦{self.balance}.")


    def transfer(self, amount, recipient, comment = ""):

        self.withdraw(amount, comment, recipient)
        recipient.deposit(amount, comment, self)

        print(f"Congrats {self.name}, your transfer of ₦{amount} to {recipient.name} was successful, your new balance is ₦{self.balance}.")
    
    def store_history(self, transaction_type, transaction_label, amount, source, comment, receiver = "Same as Sender"):
        file = open("financial statement.csv", "a")
        file.write(f"{transaction_type}, {transaction_label}, {amount}, {source}, {receiver}, {comment}\n")

        print(transaction_type, amount, comment, receiver)




atha = Account("Atha", 23, "inyangete@gmail.com", "08012345678")        

print(atha.account_no)

atha.deposit(20000)

atha.withdraw(10000)

bolu = Account("Bolu", 33,"bolu@gmail.com", "08098765432")  

atha.transfer(2000, bolu, "flexing")