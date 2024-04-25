def calculate_bmi(height, weight): 
	print("Height = " + str(height)) 
	print("Weight = " + str(weight))
	bmi=weight/(height**2)
	print("BMI = "+str(bmi))
	if bmi <18.5:
		print ("you are under weight")
	elif bmi > 25:
		print("you are over weight")
	else:
		print("you are of normal weight")
calculate_bmi(weight=57, height=1.73)
