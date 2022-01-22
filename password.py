class password:
    
  account= []

  def _init_(self,accountname,password) :

   self.accountname = accountname
   self.password = password

def save_account (self):

     password.account.append(self)

def delete_account(self):

      password.account.remove(self)

@classmethod
def display_account(cls):
    for account in cls.account:
     return cls.account

@classmethod
def find_by_accountname(cls,accountname):
   for account in cls.account:
       if account.accountname== accountname:
           return account
