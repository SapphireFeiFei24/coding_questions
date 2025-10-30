"""
Description:
You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.
Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.
Design an algorithm that:
Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
Finds the maximum price the stock has been based on the current records.
Finds the minimum price the stock has been based on the current records.

Solution
map + heap
update the min and max passively
"""
import sys
import heapq
class StockPrice:

    def __init__(self):
        self.curr_time = -1
        self.min_heap = []
        self.max_heap = []
        self.price_map = {}

    # Update price_map: O(N)
    # Update min max heap: O(logN)
    def update(self, timestamp: int, price: int) -> None:
        self.price_map[timestamp] = price
        if self.curr_time < timestamp:
            self.curr_time = timestamp

        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.price_map[self.curr_time]

    # Passive cleanup O(logN)
    def maximum(self) -> int:
        while self.max_heap:
            price, timestamp = self.max_heap[0]
            if self.price_map[timestamp] == -price:
                return -price
            heapq.heappop(self.max_heap)
        return sys.maxsize

    # Passive cleanup O(logN)
    def minimum(self) -> int:
        while self.min_heap:
            price, timestamp = self.min_heap[0]
            if self.price_map[timestamp] == price:
                return price
            heapq.heappop(self.min_heap)
        return -sys.maxsize

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
