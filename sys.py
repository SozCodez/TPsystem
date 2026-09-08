print("Welcome to Python Park!")
print("We're going to get you a ticket and check your eligibility!")

print()
print("First, enter your name ")
guestName = input(": ")

print()
print("Enter age please ")
guestAge = int(input(": "))

print()
print("How tall are you in inches ")
height = int(input(": "))

print()
print("What type of ticket did you purchase? regular or premium")
ticketType = input(": ")
while ticketType != "regular" and ticketType != "premium":
    print()
    print("That is not an option")
    ticketType = input("Please enter regular or premium: ")

print()
print("Are you a member yes/no")
pMember = input(": ")

print()
print("Will you be visiting morning or evening")
visitTime = input(": ")

def calculate_admission(age):
    if age <= 4:
       price = 0
    elif age <= 12:
        price = 15
    elif age <= 64:
         price = 30
    else:
        price = 20

    return price

admissionP = calculate_admission(guestAge)



    