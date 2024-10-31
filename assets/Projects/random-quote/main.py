import random

class QuoteGenerator:
    def __init__(self):
        self.quotes = [
            "Life is what happens when you're busy making other plans.",
            "The purpose of our lives is to be happy.",
            "Get busy living or get busy dying.",
            "You only live once, but if you do it right, once is enough."
        ]

    def get_random_quote(self):
        return random.choice(self.quotes)

def main():
    generator = QuoteGenerator()
    while True:
        input("Press Enter to get a random quote (or type 'quit' to exit): ")
        quote = generator.get_random_quote()
        print(f"Quote: {quote}")

if __name__ == "__main__":
    main()
