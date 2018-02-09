from collections import Counter

def MostPopularNumbers(array, size):
    c = Counter(array)
    values = c.most_common(size) 
    return min(values)

a = [1, 1, 2, 2, 3, 4, 5, 6] 
MostPopularNumbers(a, a.count)

