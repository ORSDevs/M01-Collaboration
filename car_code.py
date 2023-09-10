class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)


def main():
    print("Welcome to the Vehicle Information App!")
    vehicle_type = input("Please enter the vehicle type; car, truck, plane, boat, or broomstick: ")
    year = input("Please enter the year: ")
    make = input("Please enter the make: ")
    model = input("Please enter the model: ")
    doors = input("Please enter the number of doors; 0, 2, or 4: ")
    roof = input("Pplease enter the type of roof; solid or sun roof: ")

    if doors not in ["0", "2", "4"]:
        print("That is an invalid number of doors, Please enter 0, 2 or 4.")
        return

    if roof != "solid" and roof != "sun roof":
        print("That is an invalid roof type, Please enter solid or sun roof.")
        return

    automobile = Automobile(vehicle_type, year, make, model, doors, roof)

    print("\nVehicle Information:")
    automobile.display_info()


if __name__ == "__main__":
    main()