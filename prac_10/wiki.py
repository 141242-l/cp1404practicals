import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    title = input("Enter page title: ").strip()