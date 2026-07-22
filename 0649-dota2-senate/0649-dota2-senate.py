from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        n = len(senate)

        # Save each senator's position
        for index in range(n):
            if senate[index] == "R":
                radiant.append(index)
            else:
                dire.append(index)

        # Continue while both parties still have senators
        while radiant and dire:
            radiant_index = radiant.popleft()
            dire_index = dire.popleft()

            if radiant_index < dire_index:
                # Radiant acts first and bans Dire
                radiant.append(radiant_index + n)
            else:
                # Dire acts first and bans Radiant
                dire.append(dire_index + n)

        if radiant:
            return "Radiant"

        return "Dire"