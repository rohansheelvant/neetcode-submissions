class WordDictionary:

    def __init__(self):
        self.trie = {"*":{}}

    def addWord(self, word: str) -> None:
        tracking = self.trie["*"]
        for letter in word:
            if letter not in tracking:
                tracking[letter] = {}
            tracking = tracking[letter]
        
        if "*" not in tracking:
            tracking["*"] = {}
        
        return    

    def search(self, word: str) -> bool:
        tracking = self.trie["*"]

        def loop(word, tracking):
            if "." in word:
                index = word.find(".")
                prefix = word[:index]
                suffix = word[index:]

                # For Prefix
                for letter in prefix:
                    if letter not in tracking:
                        return False
                    tracking = tracking[letter]
                # Prefix succcess

                # For suffix
                if suffix:
                    possible = False
                    for letter in tracking:
                        possible = possible or loop(suffix[1:], tracking[letter])
                    
                    return possible

            else:
                prefix = word
                for letter in prefix:
                    if letter not in tracking:
                        return False
                    tracking = tracking[letter]
                return "*" in tracking
        
        return loop(word, tracking)
            
            
            


            



