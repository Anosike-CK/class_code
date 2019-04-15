
class Car:

    tyre = 4
    side_mirror = 2
    head_light = 2
    brake = 1
    light_is_on = False

    def __init__(self, color, wiper, seat_type):

        self.color = color
        self.wiper = wiper
        self.seat_type = seat_type

    def drive(self):

        print('Starting to drive')
    
    def toggle_light(self,command):

        if command == 'on':

            print('light has been turned on')
            self.light_is_on = True

        elif command == 'off':

            print('light has been turned off')
            self.light_is_on = False

# toyota = Car('blue', '2', 'leather')
# toyota.toggle_light('on')
Mercedes = Car('red', '2','leather')



