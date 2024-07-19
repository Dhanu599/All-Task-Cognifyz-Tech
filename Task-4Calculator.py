while True:
	first_no = float(input("Enter the first Number:"))
	Second_no = float(input("Enter the Second Number:"))

	ch= int(input("Enter the choices(1.Addition,2.Substraction,3.Multiplication,4.Division,5.Module):"))

	if ch in (1,2,3,4,5):
		if ch == 1:
			print(f"The Addition of Two numbers is {first_no + Second_no}.")
		elif ch == 2:
			print(f"The Substraction of Two numbers is {first_no - Second_no}.")
		elif ch == 3:
			print(f"The Multiplication of Two numbers is {first_no * Second_no}.")
		elif ch == 4:
			if Second_no == 0:
				print("Error! Division by zero is not Allowed.")
				break
			print(f"The Division of Two numbers is {first_no / Second_no}.")
		elif ch == 5:
			if Second_no == 0:
				print("Error! Module by zero is not Allowed.")
				break
			print(f"The Module of Two numbers is {first_no % Second_no}.")
	else:
		print(" You Entered the wrong choices....")
	another_calc = input("Do you want another calculation (Yes/No) : ").upper()

	if another_calc == "NO":
		break


		
