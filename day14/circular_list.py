class CircularList:
    def __init__(self, vals):
        self.data = vals

    def __getitem__(self, given):
        if isinstance(given, slice):
            return [self[x] for x in range(given.start, given.stop)]
        else:
            return self.data[given % len(self.data)]

    def __setitem__(self, given, value):
        if isinstance(given, slice):
            for i in range(given.start, given.stop):
                v = next(value)
                self[i] = v
        else:
            self.data[given % len(self.data)] = value

    def __repr__(self):
        return str(self.data)

    def reverse_portion(self, start, length):
        end = start + length
        self[start:end] = reversed(self[start:end])

