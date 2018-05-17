lookup = {}
lookup = dict()
lookup = {'age': 42}
lookup = dict(age=43)

print(lookup)
print(lookup['age'])

lookup['cat'] = 'demo code'

if 'cat' in lookup:
    print(lookup['cat'])
