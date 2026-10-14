class Codec:
    url = {}
    count = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        Codec.count += 1
        shortUrl = "TinyUrl.com" + str(Codec.count)
        Codec.url[shortUrl] = longUrl
        return shortUrl
        

    def decode(self, shortUrl: str) -> str:
        return Codec.url[shortUrl]
        """Decodes a shortened URL to its original URL.
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))