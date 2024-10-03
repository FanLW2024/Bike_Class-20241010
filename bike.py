# Lir-Wan Fan
# Purpose: Defining a Bike Class: number of gears, current gear, number of wheels, and brake type

# Properties:
# Number of Gears (1 - 15)
# Current Gear (should default to 1)
# Number of Wheels (1, 2, 3, or 4)
# Brake Type ("hand brakes" or "foot brakes")

# Methods:
# Set & Get Number of Gears:
# Set & Get Current Gear:
# Set & Get Number of Wheels:
# Set & Get Brake Type:
# Reset Gears: Set gear back to 1
# Increase Gear: Increase Current Gear by 1, do not allow going over Number of Gears
# Decrease Gear: Decrease Current Gear by 1, do not allow going under 1

###############################################
# Declaring Bike Class
class Bike:
    # Defining private properties: Using dunder
    __numberOfGears: int = 1
    __currentGear: int = 1
    __numberOfWheels = 1
    __brakeType: str = ""

    ###############################################
    # Instantiate a copy of this class
    def __init__(self, numberOfGears = 1, currentGear = 1, numberOfWheels = 1, brakeType = "hand brakes" or "foot brakes"):

        # Setting properties
        self.setNumberOfGears(numberOfGears)
        self.setCurrentGear(currentGear)
        self.setNumberOfWheels(numberOfWheels)
        self.setBrakeType(brakeType)

    ####################################################
    # Getter and Setter for the number of gears property (integer from 1 to 15)
    def getNumberOfGears(self) -> int:
        return self.__numberOfGears

    def setNumberOfGears(self, numberOfGears: int) -> None:
        try:
            if 1 <= numberOfGears <= 15:
                self.__numberOfGears = int(numberOfGears)

            elif numberOfGears > 15:
                self.__numberOfGears = 15
                self.__currentGear = 15
                print("That is the incorrect number of gears.  Number of gears must be between 1 and 15. "
                      f"Your number of gears will be set back to the max amount of {self.__numberOfGears}.")

            else:
                self.__numberOfGears = 1
                self.__currentGear = 1
                print("That is the incorrect number of gears.  Number of gears must be between 1 and 15. "
                      f"Your number of gears will be set back to the minimum amount of {self.__numberOfGears}.")

        except Exception as e:
            raise e

    ####################################################
    # Getter and Setter for the current gear property
    def getCurrentGear(self) -> int:
        return self.__currentGear

    def setCurrentGear(self, currentGear: int) -> None:
        try:
            if 1<= currentGear <= 15:
                if currentGear <= self.__numberOfGears:
                    self.__currentGear = currentGear
                else:
                    print("The set gear is higher than the amount of gears the bike has.  "
                          "Your set gear is defaulted to 1")

            else:
                print("The current gear can only be between 1-15 inclusive.  "
                      f"The current gear will be set back to default of {self.__currentGear}")

        except Exception as e:
            raise e

####################################################
# Getter and Setter for the NumberOfWheels (integer from 1 to 4)
    def getNumberOfWheels(self) -> int:
        return self.__numberOfWheels

    def setNumberOfWheels(self, numberOfWheels: int) -> None:
        try:
            if 1 <= numberOfWheels <= 4:
                self.__numberOfWheels = int(numberOfWheels)

            else:
                return print("That is the incorrect amount of wheels.  The bike can have 1-4 wheels inclusive.  "
                    f"Your number of wheels will be set back to the default amount of {self.__numberOfWheels}")

        except Exception as e:
            raise e

    ####################################################
    # Getter and Setter for the type of brakes property
    def getBrakeType(self) -> str:
        return self.__brakeType

    def setBrakeType(self, brakeType: str) -> None:
        try:
            if brakeType == "hand brakes" or brakeType == "foot brakes":
                self.__brakeType = brakeType

            else:
                print('That is the incorrect type of brakes.  These bikes can only have "hand brakes" or "foot brakes."'
                      f"Your type of breaks will be left blank until you correct the input. {self.__brakeType}")

        except Exception as e:
            raise e

    ####################################################
    # Reset Gears back to 1
    def resetGear(self, answer: str) -> None:
        try:
            answer = str(answer)
            if answer == "Yes":
                self.__currentGear = 1
                print(f"We have reset the gears back to {self.__currentGear}")

            elif answer == "No":
                print(f"We did not reset the gears, so your gear remains set at {self.__currentGear}")

            else:
                print(f'{answer} is not a valid answer.  You must type in "Yes" or "No"')

        except Exception as e:
            raise e

    ####################################################
    # Increase Gear
    def increaseGear(self, answer: str) -> None:
        try:
            answer = str(answer)
            if answer == "Yes":
                if self.__currentGear < 15 and self.__currentGear < self.__numberOfGears:
                    self.__currentGear = self.__currentGear + 1
                    print(f"We have shifted up and the current gear is now set to {self.__currentGear}")

                else:
                    print(f"We cannot shift past 15th gear or current gear of {self.__currentGear}, sorry!")

            elif answer == "No":
                self.__currentGear = self.__currentGear
                print(f"We decided not to shift up so the current gear is still {self.__currentGear}")

            else:
                print(f'{answer} is not a valid answer.  You must type in "Yes" or "No"')

        except Exception as e:
            raise e

    ####################################################
    # Decrease Gear
    def decreaseGear(self, answer: str) -> None:
        try:
            answer = str(answer)
            if answer == "Yes":
                if self.__currentGear > 1:
                    self.__currentGear = self.__currentGear - 1
                    print(f"We have shifted down and my current gear is now set to {self.__currentGear}")
                else:
                    print("We cannot shift down past 1st gear, sorry!")

            elif answer == "No":
                self.__currentGear = self.__currentGear
                print(f"We decided not to shift down so my current gear is still {self.__currentGear}")

            else:
                print(f'{answer} is not a valid answer.  You must type in "Yes" or "No"')

        except Exception as e:
            raise e


    ####################################################
    # Max Gear
    def maxGear(self, maxGear: int) -> None:
        try:
            if maxGear > 15:
                self.__maxGear = 15
                print("The max number of gear is 15.  ")

            else:
               print("The gear value must be over 1):  "
                     f"The current gear will be set back to {self.__currentGear}")

        except Exception as e:
            raise e

    ####################################################
    # Minimum Gear
    def minimumGear(self, minimumGear: int) -> None:
        try:
            if minimumGear < 1:
                self.__minimumGear = 1
                print("The minimum number of gear is 1.")

            else:
                print("The gear value must be below 1):  "
                      f"The current gear will be set back to {self.__currentGear}")

        except Exception as e:
            raise e


    ####################################################
    # Electric Brakes
    def electricBrake(self, brakeType: str) -> None:
        try:
            brakeType = str(brakeType)
            if brakeType == "electric brakes":
                print('That is the incorrect type of brakes.' 
                      'These bikes can only have "hand brakes" or "foot brakes."')

        except Exception as e:
            raise e


