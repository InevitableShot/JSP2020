class Lists:
    def __init__(self, tab):
        self.tab = tab

    def make_sublists(self):
        from itertools import combinations
        sublists = []
        for items in range(0, len(self.tab)+1):
            sublists.extend([list(item)
                             for item in combinations(self.tab, items)])
        return sublists


test_tab = Lists([1, 2, 3])
print(test_tab.make_sublists())
