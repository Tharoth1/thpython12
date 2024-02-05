# file name quiz_app.py

# get user respond

#name = input("What is your name? ") 
#print("Hello!", name)

# compare respond a answer
total_point = 0
question = input("2+2? ") 

if question == "4":
    print('Correct')
else:
    print('Incorrect')

total_point = total_point + 1 

#Q1

q = input("What is the weather today? ")

if q .lower()== 'cold':
    print("correct")
    total_point = total_point + 1
else:
    print("incorrect")

#Q2
    
q = input("When is Christmas? ")

if q .lower()== 'december':
    print("correct")
    total_point = total_point + 1
else:
    print("incorrect")

#Q3
    
q = input("What is the color of the ocean? ")

if q .lower() == 'blue':
    print("correct")
    total_point = total_point + 1
else:
    print("incorrect")

#Q4
    
q = input("What is the color of the car? ")

if q .lower() == 'pink':
    print("correct")
    total_point = total_point + 1
else:
    print("incorrect")

#Q5
    
q = input("Do i like smart? ")

if q .lower() == 'yes':
    print("correct")
    total_point = total_point + 1
else:
    print("incorrect")

print(f"Your total point is: {int(total_point/5*100)}%")


  

