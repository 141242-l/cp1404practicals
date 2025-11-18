from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def show_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

