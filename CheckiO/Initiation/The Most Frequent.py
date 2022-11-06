# https://py.checkio.org/uk/mission/the-most-frequent/

def most_frequent(data: list) -> str:
    return (most_freq_elem := {data.count(i) : i for i in set(data)})[max(most_freq_elem)]


print(most_frequent(["a", "b", "c", "a", "b", "a"]))
print(most_frequent(["a", "a", "bi", "bi", "bi"]))
