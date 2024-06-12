class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        prev_altitude = 0

        for current_altitude in gain:
            prev_altitude = prev_altitude + current_altitude # this will be like new altitude, the bike is at
            max_altitude = max(max_altitude, prev_altitude)

        return max_altitude

