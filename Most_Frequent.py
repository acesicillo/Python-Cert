#function to determine the most repeated item on a given list.
def most_frequent(data):
    return max(data, key=data.count)

data1 = ['a', 'a', 'bi', 'bi', 'bi']

most1 = most_frequent(data1)
print(most1)

data2 = ["a","a","a","b","b","c","d"]
most2 = most_frequent(data2)
print(most2)

#Assert permite realizar comprobaciones, si es False, va a retornar un "Assertion error"
assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
print('Done')