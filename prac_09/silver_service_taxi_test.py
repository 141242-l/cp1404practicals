from silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    taxi = SilverServiceTaxi("Hummer", 200, 2)

    print(taxi)

    taxi.drive(18)
    fare = taxi.get_fare()
    print(f"Fare for 18 km: ${fare:.2f}")