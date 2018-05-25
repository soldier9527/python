i = input("input your real age:")
age = int(i)
if age < 6:
    print('age=', age, '==>kid')
elif age < 18:
    print('age=', age, '==>teenager')
else:
    print('adult')
