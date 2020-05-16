import os
class BankAccount():
	#docstring for BankAccount
	def __init__(self, account_holder):
		super(BankAccount, self).__init__()
		self.account_holder = account_holder
		self.access_granted = False
		self.file_pin = 0

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
						self.file_pin = pin_number
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

	def balance(self):
		mega_list = []
		file = 'access_login.txt'
		On = True
		with open(file)as f_obj:
				for content in f_obj:
					mega_list.append(content.split())#compile megalist with smaller list created from each line of text file
		#print(f"mega_list: {mega_list}")
		while self.access_granted:
			while On:
				for sublist in mega_list:
					if self.account_holder in sublist:
						print(f"Hello {self.account_holder.title()}, your current balance is: ${sublist[-1]}.")
						On = False
						self.access_granted = False

	def deposit(self):
		print("\nIn deposit method")
		mega_list = []
		file = 'access_login.txt'
		active = 'access_login_active.txt'
		tmp = 'access_login_tmp.txt'
		On = True
		with open(file)as f_obj:
			for content in f_obj:
				mega_list.append(content.split())#compile megalist with smaller list created from each line of text file

		#print(f'Mega List: {mega_list}')
		deposit_amount = int(input("How much are you depositing? "))
		while self.access_granted:
			while On:
				for sublist in mega_list:
					if self.account_holder in sublist:
						print(f'Sub List: {sublist}')
						
						name = self.account_holder
						dep_pin_number = self.file_pin

						print(f"Hello {self.account_holder.title()}, adding ${deposit_amount} to your balance.")
						#print(sublist[2])
						final_deposit_value = int(sublist[2]) + deposit_amount
						deposit_add = str(final_deposit_value)

						mega_list.remove(sublist) #remove active sublist/megalist index to only focus on adding other indexes to text file records
						#print(f"Updated Mega List {mega_list}")

						#Write to temp file after converting indexes (sublist) into string seperated by white_space
						with open(tmp,'w')as f_obj:
							for line in mega_list:
								unlist = ' '.join(line) #Using join method to change make sublist/index of megalist mimic a string
								#print(f"Unlist: {unlist}")
								f_obj.write(unlist+'\n')

						#Used to read content of temp file as a method of copying content
						with open(tmp)as f_obj:
							tpm_content = f_obj.read()
							#print(f"TPM CONTENT: \n{tpm_content}")

						#Write temp file content to active_file 
						with open(active,'w')as f_obj:
							f_obj.write(tpm_content)
						
						#Append active name, pin, and new deposit as a method of replacing entire line for user logged in.
						with open(active,'a') as f_obj:
							f_obj.write(name+' '+str(dep_pin_number)+' '+str(final_deposit_value))
							On = False
						self.access_granted = False

						#copy active to login file to update main file
						os.system('cp access_login_active.txt access_login.txt')

	def withdraw(self):
		print('na')

def main():
	justin = BankAccount('kera')
	justin.login()
	justin.balance()
	justin.login()
	justin.deposit()
	justin.login()
	justin.balance()

main()
