from UAV import UAV
#subclass
class Drone(UAV):
    def __init__(self, name):
        self.name = name

    def takeoff(self):
        #if landing don't change anything
        if(self.is_landing):
            return False

        self.is_takeoff = False if self.is_landing else True
        return self.is_takeoff