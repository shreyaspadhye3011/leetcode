# Build a hash table representing the state of a DB from a given list of operations: "EPOCH|TYPE|KEY|VAL"
import fileinput
import datetime
class HashTable:
    def __init__(self, rawEvents):
        """ Build a HashTable from a list of raw pipe-delimited DML Events """
        self.rawEvents = rawEvents
        self.HashTable = {}

    @property
    def table(self):
        """ Retrieve the current state of the HashTable

        Returns
        -------
        dict(str, str): the key-value pairs
        """
        for event in self.rawEvents:
            event_split = event.split("|")
            if len(event_split) == 4:
                action = event_split[1]
                key = event_split[2]
                val = event_split[3]
                
                if action == "INSERT":
                    if key not in self.HashTable:
                        self.HashTable[key] = val
                elif action == "UPSERT":
                    self.HashTable[key] = val
                elif action == "DELETE":
                    del self.HashTable[key]
        return self.HashTable

    @property
    def high_watermark(self):
        """ Retrieve the high-watermark of the system  -- the UTC epoch millisecond timestamp of the latest 
        event read as a datetime or datetime.datetime.utcfromtimestamp(0) (Epoch 0) if no event occurred

        Returns
        -------
        datetime.datetime: the high-watermark
        """
        watermark = 0

        if not self.rawEvents:
            return datetime.datetime.utcfromtimestamp(0)

        for event in self.rawEvents:
            rawEvent = int(event.split("|")[0])
            if rawEvent > watermark:
                watermark = rawEvent

        return  datetime.datetime.fromtimestamp(watermark/1000.0)
    
obj = HashTable(["1563454984001|INSERT|test|123", "1563454984002|INSERT|test|321"])
obj.table