from itertools import combinations


class StringClass:
    def __init__(self):
        self.inp = "12345"

    def get_length(self):
        return len(self.inp)

    def get_list_of_char (self):
        return [char for char in self.inp]


class PairsPossible (StringClass):
    pairs =[]

    def store_possible_pairs(self):
        pairs = list(combinations(self.inp, 2))

    def print_list_of_all_possible_pairs(self):
        for i in self.pairs:
            print(self.pairs[i])


class SearchCommonElements:
    def __init__(self):
        self.inp2 = "34567"

    def find_common_elements(self):
        common_elements = []
        sc = StringClass()
        inp2_as_set = set([char for char in self.inp2])
        intersection = inp2_as_set.intersection(sc.get_list_of_char())
        intersection_as_list = list(intersection)
        return intersection


class EqualSumPairs:
    def get_total_pairs(self):
        pp = PairsPossible()
        return len(pp.pairs)


sce = SearchCommonElements()
print("Common Elements:")
print(sce.find_common_elements())

eps = EqualSumPairs()
print ("Result from Equal Sum Pairs:")
print(eps.get_total_pairs())





