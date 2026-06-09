class PrefixTree:

    def __init__(self):
        self.trie = {"*":{}}    

    def insert(self, word: str) -> None:
        tracking = self.trie["*"]
        for letter in word:
            if letter in tracking:
                tracking = tracking[letter]
            else:
                tracking[letter] = {}
                tracking = tracking[letter]
        
        if "*" not in tracking:
            tracking["*"] = {}
        
        return

    def search(self, word: str) -> bool:
        tracking = self.trie["*"]
        for letter in word:
            if letter not in tracking:
                return False
            else:
                tracking = tracking[letter]
        
        return "*" in tracking
        

    def startsWith(self, prefix: str) -> bool:
        tracking = self.trie["*"]
        for letter in prefix:
            if letter not in tracking:
                return False
            else:
                tracking = tracking[letter]
        
        return True
        
        