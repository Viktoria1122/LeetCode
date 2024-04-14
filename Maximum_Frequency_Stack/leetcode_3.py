from collections import defaultdict, deque

class FreqStack:

    def __init__(self):
        self.freq_map = defaultdict(int)
        self.group = defaultdict(deque)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq_map[val] += 1
        freq = self.freq_map[val]
        self.max_freq = max(self.max_freq, freq)
        self.group[freq].append(val)

    def pop(self) -> int:
        most_freq_vals = self.group[self.max_freq]
        popped_val = most_freq_vals.pop()
        if not most_freq_vals:
            del self.group[self.max_freq]

        self.freq_map[popped_val] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return popped_val