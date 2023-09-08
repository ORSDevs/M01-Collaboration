def good():
    return ['Harry', 'Ron', 'Hermione']

def get_odds():
    for number in range(1, 10, 2):
        yield number

result = good()
print(result)

count = 0
for odd in get_odds():
    count += 1
    if count == 3:
        print(odd)
        break