# Lir-Wan Fan
# Purpose: Creating a Bike Class using different inputs and values

# Import our bike class from bike.py
from bike import Bike

###############################################
# Instantiate a Bike object
###############################################

try:
    # Giant
    giant = Bike(15, 1, 2, "hand brakes")

    # Giant
    # Now, instantiating a Bike object with no information initially.
    #  Then, add that information after the object has been created.
    giant = Bike()
    giant.setNumberOfGears(15)
    giant.setCurrentGear(1)
    giant.setNumberOfWheels(2)
    giant.setBrakeType("hand brakes")

    # Printing bike info
    print(f"The Bike information:")
    print(f"The Number of Gears is: {giant.getNumberOfGears()}")
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    print(f"The Number of Wheels is: {giant.getNumberOfWheels()}")
    print(f"The Brake Type is: {giant.getBrakeType()}")
    input("Press [Enter] to continue\n")
    print()

    ###############################################
    # 2) Set Gear to 10
    giant = Bike(15, 10, 2, "hand brakes")
    giant = Bike()
    giant.setNumberOfGears(15)
    giant.setCurrentGear(10)
    giant.setNumberOfWheels(2)
    giant.setBrakeType("hand brakes")

    # Printing bike info
    print(f"The Current Gear set to 10.")
    input("Press [Enter] to continue\n")
    print()
    print(f"The Bike information:")
    print(f"The Number of Gears is: {giant.getNumberOfGears()}")
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    print(f"The Number of Wheels is: {giant.getNumberOfWheels()}")
    print(f"The Brake Type is: {giant.getBrakeType()}")
    input("Press [Enter] to continue\n")
    print()

    ###############################################
    # Resetting gear back to 1
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    input("Press [Enter] to continue\n")
    print()
    giant.resetGear((input('Would you like to reset the gear back to 1, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    input("Press [Enter] to continue\n")
    print()

    ###############################################
    # 3) Increase Gear
    giant.increaseGear((input('Would you like to increase the gear by 1, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.increaseGear((input('Would you like to increase the gear by 1, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.increaseGear((input('Would you like to increase the gear by 1, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.increaseGear((input('Would you like to increase the gear by 1, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.increaseGear((input('Would you like to increase the gear by 1, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.increaseGear((input('Would you like to increase the gear by 1, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.increaseGear((input('Would you like to increase the gear by 1, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.increaseGear((input('Would you like to increase the gear by 1, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.increaseGear((input('Would you like to increase the gear by 1, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.increaseGear((input('Would you like to increase the gear by 1, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.increaseGear((input('Would you like to increase the gear by 1, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.increaseGear((input('Would you like to increase the gear by 1, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.increaseGear((input('Would you like to increase the gear by 1, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.increaseGear((input('Would you like to increase the gear by 1, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")

    input("Press [Enter] to continue\n")
    print()

    ###############################################
    # Decrease Gear
    giant.decreaseGear((input('Would you like to decrease the gear, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.decreaseGear((input('Would you like to decrease the gear, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.decreaseGear((input('Would you like to decrease the gear, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.decreaseGear((input('Would you like to decrease the gear, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.decreaseGear((input('Would you like to decrease the gear, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.decreaseGear((input('Would you like to decrease the gear, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.decreaseGear((input('Would you like to decrease the gear, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.decreaseGear((input('Would you like to decrease the gear, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.decreaseGear((input('Would you like to decrease the gear, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.decreaseGear((input('Would you like to decrease the gear, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.decreaseGear((input('Would you like to decrease the gear, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.decreaseGear((input('Would you like to decrease the gear, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.decreaseGear((input('Would you like to decrease the gear, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    giant.decreaseGear((input('Would you like to decrease the gear, "Yes" or "No?" ')))
    print(f"The Current Gear is: {giant.getCurrentGear()}")

    input("Press [Enter] to continue\n")
    print()

    ###############################################
    # 4) Max Gear
    maxGear = int(input("Please enter a gear value of gear (must be over 15): "))
    giant.setNumberOfGears(maxGear)
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    input("Press [Enter] to continue\n")
    print()

    ###############################################
    # 4) Minimum Gear
    minimumGear = int(input("Please enter a small value of gear (must be below 1): "))
    giant.setNumberOfGears(minimumGear)
    print(f"The Current Gear is: {giant.getCurrentGear()}")
    input("Press [Enter] to continue\n")
    print()

    ###############################################
    # 5) Electric Brakes
    giant.electricBrake((input('Please enter the brake type (must be “electric brakes”): ')))

    input("Press [ENTER] to finish \n")
    print("FINISHED")

    # Catching exception
except Exception as e:
    print(f"Got an error: {e}")
