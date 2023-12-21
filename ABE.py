import os # To use the type command and easily display a text file's contents

# display the main menu of the program
def menu_display():	
	os.system("cls")
	print ("BULK EMAILING PROGRAM\n---------------")
	print ("Please enter the number corresponding to the menu option you want to choose:")
	print ("\t1) Instructions")
	print ("\t2) Settings")
	print ("\t3) Blah")
	print ("\t4) Blah")
	print ("\t5) Blah")
	print ("\t6) Quit")



# Take an integer as a menu choice
while True:
	menu_display()
	menu_choice = int(input())
	os.system("cls")
	if menu_choice == 1:	
		os.system("type instructions.txt")
		unused_variable = input()
	elif menu_choice == 2:
		submenu_choice = 0
		while submenu_choice != 3:
			print("SETTINGS")
			print("1)\tChange email context (text) ")
			print("2)\tChange other settings")
			print("3)\tQuit")
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
		pass

	elif menu_choice == 4:
		pass

	elif menu_choice == 5:
		pass

	elif menu_choice == 6:
		exit()

	else:
		print("Invalid choice.")
		unused_variable = input()

