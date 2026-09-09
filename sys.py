#park introduction
print("Welcome to Python Park!")
print("We're going to get you a ticket and check your eligibility!")

#gathering guest data
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

print()
print("Are you spervised? y/n")
supervised = input(": ")
if supervised == "y":
    boolSupervised = True
elif supervised == "n":
    boolSupervised = False

#admission price function
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

#discount function
def calculateDis(price, member, visitTime):
    if member == "yes":
        discount = price - 5
    if visitTime == "evening":
        discount = price - 3
    if member == "yes" and visitTime == "evening":
        discount = price - 10
    if member == "no" and visitTime == "morning":
        discount = price

    return discount

discountedP = calculateDis (admissionP, pMember, visitTime)

#preventing negative prices
if discountedP <= 0:
    discountedP = 0

#ride function
def rideLevel(height, age):
    if height >= 54 and age >= 16:
        level = "Extreme Rides"
    elif height >= 48 and age >= 12:
        level = "Thrill Rides"
    elif height >= 42 and age >= 8:
        level = "Family Rides"
    elif height >= 36 and age >= 0:
        level = "Kiddie Rides"
    else:
        level = "No Rides"

    return level

level = rideLevel(height, guestAge)

#supervision
def checkSupervision(age, visitingWadult):
    if age < 13 and visitingWadult == False:
        supervision = "Adult Required"
    elif age < 13 and visitingWadult == True:
        supervision = "Approved"
    elif age >= 13 and visitingWadult == False:
        supervision = "Approved"
    else:
        supervision = "Approved"
    
    return supervision

supervisionStat = checkSupervision(guestAge, boolSupervised)

#premium ticket check
premiumB = "No Bonus :("
if ticketType == "premium":
    
    premiumB = "Premium Bonus! Free meal, usable once per day"
#above, check also adds str to variable for finalReport

def checkVip(ticket, parkM, age):
    if ticket == "premium" and parkM == "yes":
        access = "VIP Access"
    elif age >= 65 and ticket == "premium":
        access = "VIP Access"
    else:
        access = "STANDARD Access"

    return access

vipStatus = checkVip(ticketType, pMember, guestAge)

#final report function
def finalReport(guest):
    print()
    print("----- Python Park -----")
    print("----- Guest Report -----")
    print()
    print("Guest: ", guestName)
    print(vipStatus)
    print()
    print("Age: ", guestAge)
    print("Height: ", height, " inches")
    print("Ticket Type: ", ticketType)
    print("Membership: ", pMember)
    print()
    print()
    print("Regular Admission: ", admissionP)
    print("Discounted Admission: ", discountedP)
    print()
    print("Supervision Status: ")
    print(supervisionStat)
    print("Highest Ride Level: ")
    print(level)
    print()

    #personalized message
    print(premiumB)
    print()
    print("-- Enjoy Python Park! --")
    print()

finalReport(guestName)