class RecentCounter:

    def __init__(self):
        self.recent_requests = []

    def ping(self, t: int) -> int:
        self.recent_requests.append(t) # add new requests to the list
        
        while self.recent_requests and self.recent_requests[0] < t-3000:
            self.recent_requests.pop(0)
            
        return len(self.recent_requests)
        # flush the values, we dont need anymore
        for i in self.recent_requests:
            if i >= t-3000: # latest values starts from here
                return len(self.recent_requests)
            self.recent_requests.pop(0) # pop the values which are older than 3 seconds

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# class RecentCounter:

#     def __init__(self):
#         self.recent_requests = []

#     def ping(self, t: int) -> int:
#         self.recent_requests.append(t) # add new requests to the list

#         # flush the values, we dont need anymore
#         for index, i in enumerate(self.recent_requests):
#             if i >= t-3000: # latest values starts from here
#                 self.recent_requests = self.recent_requests[index:] # flush the old values and keep only the latest value
#                 total_request =  len(self.recent_requests)
#                 return total_request