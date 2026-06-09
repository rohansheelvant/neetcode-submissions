class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.track = {}
        self.stack = []
        self.time = 0
        

    def get(self, key: int) -> int:
        if key in self.mapping:
            self.track[key] = self.time
            self.stack.append([key, self.time])
            self.time += 1
            return self.mapping[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        # Do not evict
        if len(self.mapping) != self.capacity:
            self.mapping[key] = value
            self.track[key] = self.time
            self.stack.append([key, self.time])
            self.time += 1
        elif key in self.mapping:
            self.mapping[key] = value
            self.track[key] = self.time
            self.stack.append([key, self.time])
            self.time += 1
        else:
            while(self.stack):
                key1, time1 = self.stack.pop(0)
                if time1 == self.track[key1]:
                    break
        
            del self.mapping[key1]

            self.mapping[key] = value
            self.track[key] = self.time
            self.stack.append([key, self.time])
            self.time += 1

        print(self.mapping)
