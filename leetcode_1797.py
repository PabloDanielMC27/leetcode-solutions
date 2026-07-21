# 1797. Design Authentication Manager

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.cache = OrderedDict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        time = currentTime + self.ttl
        self.cache[tokenId] = time

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.cache.get(tokenId) and self.cache[tokenId] > currentTime:
                time = currentTime + self.ttl
                self.cache[tokenId] = time

    def countUnexpiredTokens(self, currentTime: int) -> int:

        # unefficient version
        for key in list(self.cache):
            if self.cache[key] <= currentTime:
                del(self.cache[key])      
        return len(self.cache.items())


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
