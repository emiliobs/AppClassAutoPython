from Auto import Auto


car = Auto("Toyota", "Camry", 2020, 0)
print(f"Velocidad Actual: {car.get_speed()}, mph ")
print()

print("=======================================")
car.acelerate()
car.acelerate()
print(f"Velocidad Actual: {car.get_speed()}, mph")
print()
print("========================================")
car.brake()
print(f"Velocidad Actual: {car.get_speed()} mph")
print()