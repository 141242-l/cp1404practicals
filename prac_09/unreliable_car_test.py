from unreliable_car import UnreliableCar

def test_unreliable_car():
    """Test driving behavior of UnreliableCar with different reliability levels."""
    low_reliability_car = UnreliableCar("LowReliability", 100, 10)
    high_reliability_car = UnreliableCar("HighReliability", 100, 90)

    low_drive_count = 0
    high_drive_count = 0
    test_attempts = 100