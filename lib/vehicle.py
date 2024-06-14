class Vehicle:
        def __init__(self,wheel_size,wheel_number):
            self.wheel_size = wheel_size
            self.wheel_number = wheel_number
        
        # @property
        # def wheel_size(self):
        #     return self._wheel_size
        
        # @wheel_size.setter
        # def wheel_size(self,wheel_size):
        #     self._wheel_size = wheel_size
        
        # @property
        # def wheel_number(self):
        #     return self._wheel_number 
        
        # @wheel_number.setter
        # def wheel_number(self,wheel_number):
        #     self._wheel_number = wheel_number

        
        def go(self):
            return "vrrrrrrrooom!"
        
        def fill_up_tank(self):
            return "filling up!"