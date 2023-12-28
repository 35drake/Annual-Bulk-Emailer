import os # For command-line and printing commands

# The main component of the program. It automatically sends emails asking for documents, processes documents that you've received/downloaded,
#	prints them, and updates the spreadsheet when you upload them to your online database. It also reminds you when documents are
# 	to be uploaded. NOTE: Before it completes any email or printing, it will ask you for confirmation.
def wizard():
	backup_spreadsheet()
	a=input()
	# get the spreadsheet as a NumPy array 
	SS = pandas.read_excel("Spreadsheet.xlsx").to_numpy()
	print(SS)
	print(type(SS))
	
	#Now, do the following:
		# Print any correctly-named documents that have come in folder 1A, then check them off the spreadsheet.
		# whatever incorrectly-named documents there are, place them in folder 1B and notify the user.
		# Create recommended emails with attachments(don't send, but assume that the user did send them)
		# PROGRAM HERE DRAKE
	
	unused_variable = input()


# Overwrite the old backup spreadsheet every time a new set of spreadsheet of operations is completed and checked off the sheet.
# (ie a bunch of prints or a bunch of emails). I don't wanna wait till BOTH sets of operations are done before backup up, because 
# then if there's a problem with one and not the other, we could be left with only a backup that's too outdated to fall back on.
def backup_spreadsheet():
	# Copy the Spreadsheet file as a backup, and overwrite the previous backup if one exists
	# For some reason I can't figure out how to both copy and rename a file in a single cmd command
	os.system("copy Spreadsheet.xlsx Backup.xlsx /Y")
	os.system("move Backup.xlsx files") # moving it into the "files" folder




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
		while submenu_choice != 4:
			print("SETTINGS")
			print("1)\tChange email context (text) ")
			print("2)\tChange variables")
			print("3)\tReset variables to default")
			print("4)\tQuit\n")
			submenu_choice = int(input())
			os.system("cls")
			if submenu_choice == 1:
				os.system("notepad \"files/Email Text Content.txt\"")
			elif submenu_choice == 2:
				os.system("notepad files/variables.txt")
			elif submenu_choice == 3:
				# I still have no idea why sometimes only forward slashes work in cmd and sometimes it's only backslashes
				os.system("del files\\variables.txt /Q")
				text_file = open("files\\variables.txt", "w")
				text_file.write("current_year_or_quarter = 2023\nmy_name = Drake\nblank_variable = 0")
				text_file.close()
				os.system("cls")
				print("Variables reset to defaults.")
				unused_variable = input("Press Enter to continue.")
			elif submenu_choice == 4:
				pass
			else:
				print("Ivalid choice.")
				unused_variable = input()

	elif menu_choice == 3:
		wizard()

	elif menu_choice == 4:
		os.system("cls")
		print_choice = input("Would you like to run test prints? (Y/n) ")
		if print_choice == "Y" or print_choice == "y":
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



