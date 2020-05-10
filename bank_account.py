class BankAccount():
	#docstring for BankAccount
	def __init__(self, account_holder):
		super(BankAccount, self).__init__()
		self.account_holder = account_holder
		self.access_granted = False

	def login(self):
		mega_list = []
		incorrect_attempts = 1
		file = 'access_login.txt'
		On = True
		with open(file)as f_obj:
				for content in f_obj:
					mega_list.append(content.split())#compile megalist with smaller list created from each line of text file
		while On:
			for sublist in mega_list:
				if self.account_holder in sublist:
					print(f'Hello {self.account_holder.title()}, verify access by entering pin.')
					pin_number = int(input("Please enter your pin number to login: "))
					if str(pin_number) in sublist:
						self.access_granted = True
						print("Access Granted")
						On = False
					else:
						print("Access Denied")
						incorrect_attempts+=1
						print(f"You have {4-incorrect_attempts} more tries before locking account.")
						if incorrect_attempts>3:
							print(f"Locking {self.account_holder.title()}'s account.")
							On = False
						else:
							continue
				else:
					continue #just continue if currenet account_holder can't be found in current list



	def deposit(self):
		while self.access_granted:
			deposit_amount = int(input("How much are you depositing? "))
			balance+=deposit_amount
			self.access_granted = False

	def withdraw(self):
		print('na')

	def balance(self):
		print('na')

def main():
	justin = BankAccount('zeke')
	justin.login()

main()
