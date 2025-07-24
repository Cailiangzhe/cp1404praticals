from unreliable_car import UnreliableCar

def test_unreliable_car():
    """Test if the unreliable car can drive"""
    car = UnreliableCar("MaybeMobile", 100, 30)
    total_drive_attempts = 100
    successful_drives = 0
    total_distance_driven = 0

    for _ in range(total_drive_attempts):
        distance = car.drive(1)
        if distance > 0:
            successful_drives += 1
            total_distance_driven += distance

    print(f"Tried driving {total_drive_attempts} times at 30% reliability")
    print(f"Successful drives: {successful_drives}")
    print(f"Total distance driven: {total_distance_driven}")
    print(f"Final odometer reading: {car.odometer}")
    print(f"Remaining fuel: {car.fuel}")

if __name__ == '__main__':
    test_unreliable_car()
