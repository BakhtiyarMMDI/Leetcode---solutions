from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:

        # Add the new request
        self.queue.append(t)

        # Remove old requests
        while self.queue[0] < t - 3000:
            self.queue.popleft()

        # Return how many requests remain
        return len(self.queue)