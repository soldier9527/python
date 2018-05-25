pdict = {
    'Michael':95,
    'Bob':70,
    'Lucy':100
}

print(pdict)
print(pdict['Bob'])
# print(pdict['haha'])

print('haha' in pdict)

print(pdict.get('haha'))
print(pdict.get('haha2',-1))
print(pdict.get('Bob',-1))