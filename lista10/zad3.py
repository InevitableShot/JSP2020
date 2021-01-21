class Lists:
    def __init__(self, tab):
        self.tab = tab

    def find_triple_sublists_equaled_zero(self):
        from itertools import combinations
        from math import fsum
        if len(self.tab) < 3:
            return "Lista jest zbyt krótka do wykonania tej metody."
        else:
            sublists = [list(item) for item in combinations(
                self.tab, 3) if fsum(item) == 0]
            return "Ta lista nie posiada podlist spełniających warunek." if len(sublists) == 0 else sublists


test_tab = Lists([1, -2.5, 1.5, 4, -5])
print(test_tab.find_triple_sublists_equaled_zero())
