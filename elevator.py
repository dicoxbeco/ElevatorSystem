from collections import Counter

# TODO: See below list
#   - Generate log files of the current operations
#   - Import/Export the file upon user-triggered start/end of the program
#   - Sort destination floor based on direction and proximity  
#
# LONG TERM GOAL: Scale out to multiple elevator management, store files in DB and Blob

class Elevator():
    def __init__(self, status, currentFloor, numPassenger, operations):
        self.status = status
        self.currentFloor = currentFloor
        self.numPassenger = numPassenger
        self.operations = operations
        #self.maxCapacity = maxCapacity
    
    # recursion for each floor stop?
    # store floor stop to operations constructor to save progress
    def operate(newPassenger, destFloor):
        numPassenger += newPassenger
        # for loop to check current floor vs. next destination floor
        # pring going up/down based on result
        #for x in operat 

    def importElevator(self):
        #CODE ME   
        return

    def exportElevator(self):
        #CODE ME
        return

    def exitElevator(self):
        print("Opening door.", end=' ') 
        if str(self.currentFloor) in self.operations:
            del self.operations[str(self.currentFloor)]
            print("Passengers leaving elevator.")

    def enterElevator(self):
        operations = {}
        while True:
            newDest = input("Which floor? (+int for above ground and -int for underground. If none, type 0): ")
            try:
                val = int(str(newDest))
            except ValueError:
                print("Invalid input")
                continue

            if int(str(newDest)) == 0:
                print("Closing door. Moving to the destination floor.")
                print("Total passnegers: " + str(self.numPassenger))
                if (len(self.operations) == 0):
                    self.operations = operations
                else:
                    self.operations = Counter(self.operations) + Counter(operations)
                break
            elif int(str(newDest)) == self.getCurrentFloor():
                print("Already at the current floor.")
                continue
            elif int(str(newDest)) < 0:
                newDest = "B" + str(abs(newDest))
            
            if newDest in operations:               
                operations[newDest] += 1
            else:
                operations[newDest] = 1

            self.numPassenger += 1
            print(operations)

    def moveElevator(self): 
        if self.status == "idle":
            return

print("Importing file...", end=' ')
print("successful")
print("Elevator is operational")

elevator = Elevator("idle", 1, 0, {"1":2})
elevator.exitElevator()
elevator.enterElevator()