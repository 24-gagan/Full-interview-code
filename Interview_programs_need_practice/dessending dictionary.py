from operator import itemgetter  # itemgetter is used to get

data = {"a": 3, "b": 1, "c": 2}  # dictionary

sorted_dict = dict(
    sorted(data.items(), key=itemgetter(1), reverse=True)
)  # creating dictioary and sorting in the reverse order and itemgetter get the index value

print(sorted_dict)  # Print the sorted dictionary
