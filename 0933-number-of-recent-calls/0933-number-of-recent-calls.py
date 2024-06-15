class RecentCounter:

    def __init__(self):
        self.recent_requests = []

    def ping(self, t: int) -> int:
        self.recent_requests.append(t) # add new requests to the list

        # flush the values, we dont need anymore
        for index, i in enumerate(self.recent_requests):
            if i >= t-3000: # latest values starts from here
                self.recent_requests = self.recent_requests[index:] # flush the old values and keep only the latest value
                total_request =  len(self.recent_requests)
                return total_request

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)