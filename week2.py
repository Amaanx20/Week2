name = input("Whats your name?")
print("Hello there,", name, "Good to meet you.")

dog = float(input("Enter the temp in Celsius:"))
fahrenheit = (dog * 1.8 + 32)
print(dog, " Celsius is equivalent to", fahrenheit, "In Fahrenheit")

students = int(input("How many students are there?"))
groups = int(input("What's your group size?"))
fox = (students//groups)
rat = fox
bat = (students % groups)
print("There will be", fox, "groups with", bat, "Students left over.")

eagle = int(input("How many sweets?"))
beagle = int(input("How many kids?"))
regal = (eagle//beagle)
racoon = (eagle % beagle)
print("there are", beagle, "kids and each kid gets", regal, "Sweets, There are", racoon, "Sweets left over")