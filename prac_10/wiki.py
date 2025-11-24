import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(f"\n{page.title}")
            print(f"{page.summary}\n")
            print(page.url)