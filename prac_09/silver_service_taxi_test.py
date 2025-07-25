from silver_service_taxi import SilverServiceTaxi


def test_silver_service_taxi():
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.drive(18)
    fare = taxi.get_fare()
    print(taxi)
    print(f"Fare: ${fare:.2f}")

    assert round(fare, 2) == 48.80, f"Expected $48.80, got ${fare:.2f}"


if __name__ == '__main__':
    test_silver_service_taxi()
