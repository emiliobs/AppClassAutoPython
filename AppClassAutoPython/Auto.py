class Auto:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def acelerate(self):
        self.speed += 5

    def brake(self):
        self -= 5

    def get_speed(self):
        return self.speed



