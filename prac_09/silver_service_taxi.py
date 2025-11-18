from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        price = Taxi.price_per_km * fanciness
        super().__init__(name, fuel, price)
        self.fanciness = fanciness