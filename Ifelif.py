print("--------------------------------------------------------")
print("----------------Ticket Booking System-------------------")
print("--------------------------------------------------------")

print ("Please enter your age: ")
Age = int(input())

if Age <= 5:
    print("You are eligible for a free ticket.")
elif Age > 5 and Age <= 18:
    print("Your ticket price is 900.")
elif Age > 18 and Age <= 40:
    print("Your ticket price is 1200.")
else:
    print("Your ticket price is 1500.")