import random
import string

class URLShortener:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "http://short.url/"

    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(6))

    def shorten_url(self, long_url):
        if long_url in self.url_to_code:
            return self.base_url + self.url_to_code[long_url]
        
        short_code = self.generate_short_code()
        self.url_to_code[long_url] = short_code
        self.code_to_url[short_code] = long_url

        return self.base_url + short_code

    def expand_url(self, short_url):
        short_code = short_url[len(self.base_url):]
        if short_code in self.code_to_url:
            return self.code_to_url[short_code]
        else:
            return "Short URL not found."

# Usage example
if __name__ == "__main__":
    url_shortener = URLShortener()

    long_url = "https://www.example.com/long/url/to/be/shortened"
    short_url = url_shortener.shorten_url(long_url)
    print("Short URL:", short_url)

    original_url = url_shortener.expand_url(short_url)
    print("Original URL:", original_url)
