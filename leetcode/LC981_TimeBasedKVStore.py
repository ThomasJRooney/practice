class TimeMap:

    def __init__(self):
        self.mapy = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.mapy:
            self.mapy[key][timestamp] = value
        else:
            self.mapy[key] = {timestamp : value}

    def get(self, key: str, timestamp: int) -> str:
		# if key not present
        if key not in self.mapy:
            return ''
        # finding timestamp_prev <= timestamp
        while (timestamp not in self.mapy[key]) and timestamp > 0:
            timestamp -= 1
        # if timestamp not present
        if timestamp == 0:
            return ''
        
        # print(self.mapy[key][timestamp])
        
        return self.mapy[key][timestamp]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)