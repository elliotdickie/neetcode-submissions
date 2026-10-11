class TimeMap:
    #hashmap
    #key is key
    #value is array of timestamps and values
    def __init__(self):
        self.key_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.key_map:
            self.key_map[key].append([timestamp,value])
        else:
            self.key_map[key] = [[timestamp,value]]

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.key_map: return res
        timestamps = self.key_map[key]
        l = 0
        r = len(timestamps)-1
        while l <= r:
            m = l+(r-l)//2
            if timestamps[m][0] <= timestamp:
                res = timestamps[m][1]
                l=m+1
            else:
                r = m -1
        return res
