class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad, dir = deque(), deque()

        # populate the queue
        for index, char in enumerate(senate):
            if char == 'R':
                rad.append(index)
            else:
                dir.append(index)

        n = len(senate)

        # make turn
        while rad and dir:
            r = rad.popleft()
            d = dir.popleft()

            if r < d:
                rad.append(r + n)
            else:
                dir.append(d + n)

        return "Radiant" if rad else "Dire"
