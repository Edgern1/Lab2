def calculate_bmi(height, weight): 
	print("Height = " + str(height)) 
	print("Weight = " + str(weight))
	bmi=weight/(height**2)
	print("BMI = "+str(bmi))
	if bmi <18.5:
		#print ("you are under weight")
		return -1
	elif bmi > 25:
		#print("you are over weight")
		return 0
	else:
		#print("you are of normal weight")
		return 1
