import os # For command-line and printing commands

# The main component of the program. It automatically sends emails asking for documents, processes documents that you've received/downloaded,
#	prints them, and updates the spreadsheet when you upload them to your online database. It also reminds you when documents are
# 	to be uploaded. NOTE: Before it completes any email or printing, it will ask you for confirmation.
def wizard():
	# get the spreadsheet as a NumPy array 
	SS = pandas.read_excel("Spreadsheet.xlsx").to_numpy()
	print(SS)
	unused_variable = input()


# Print a document (the default printer must already be set properly)
def print_document(document_name):
	try:
		os.startfile(document_name,"print")
		return "success"
	except:
		return "failure"

# display the main menu of the program
def menu_display():	
	os.system("cls")
	print ("BULK EMAILING PROGRAM\n---------------")
	print ("Please enter the number corresponding to the menu option you want to choose:")
	print ("\t1) Instructions")
	print ("\t2) Settings")
	print ("\t3) Run emailing and document-processing wizard")
	print ("\t4) Run Test Prints")
	print ("\t5) Blank")
	print ("\t6) Quit\n")

	
# Install the necessary libraries for this program. I couldn't figure out how to make this iterate over a list of the libraries
try:
	import pandas
except ModuleNotFoundError:
	print("\nYour computer needs a Python library called \"pandas\" to run this program properly.")
	install_choice = input("Would you like to install pandas? (Y/n) ")
	if install_choice == "Y" or install_choice == "y":
		print("Pandas is being installed...")
		os.system("pip install pandas")
		import pandas
		os.system("cls")
		unused_variable = input("Done downloading pandas. Press any key to continue.")
	else:
		print("\nProgram ended.")
		exit()
try:
	import openpyxl
except ModuleNotFoundError:
	print("\nYour computer needs a Python library called \"openpyxl\" to run this program properly.")
	install_choice = input("Would you like to install openpyxl? (Y/n) ")
	if install_choice == "Y" or install_choice == "y":
		print("Openpyxl is being installed...")
		os.system("pip install openpyxl")
		import openpyxl
		os.system("cls")
		unused_variable = input("Done downloading openpyxl. Press any key to continue.")
	else:
		print("\nProgram ended.")
		exit()




# Take an integer as a menu choice
while True:
	menu_display()
	menu_choice = int(input())
	os.system("cls")
	if menu_choice == 1:	
		print("See instructions in the popup window.\nPress Enter when done.")
		os.system("notepad instructions.txt")
		unused_variable = input()
	elif menu_choice == 2:
		submenu_choice = 0
		while submenu_choice != 3:
			print("SETTINGS")
			print("1)\tChange email context (text) ")
			print("2)\tChange other settings")
			print("3)\tQuit\n")
			submenu_choice = int(input())
			os.system("cls")

			if submenu_choice == 1:
				os.system("notepad \"files/Email Text Content.txt\"")
			elif submenu_choice == 2:
				os.system("notepad files/variables.txt")
			elif submenu_choice == 3:
				pass
			else:
				print("Ivalid choice.")
				unused_variable = input()

	elif menu_choice == 3:
		wizard()

	elif menu_choice == 4:
		os.system("cls")
		print("Running test prints. Make sure that the default printer and print settings are ")
		print("set properly for both the Word Doc and PDF prints.")
		print("Word Doc printing",print_document("files\\Test-Prints\\Word-Doc-Test.docx"))  # I'm not sure why slashes don't work here and only double-backslashes do
		print("PDF printing",print_document("files\\Test-Prints\\PDF-Test.PDF"))
		unused_variable = input("Press Enter to continue.")

	elif menu_choice == 5:
		pass		

	elif menu_choice == 6:
		exit()

	else:
		print("Invalid choice.")
		unused_variable = input()



