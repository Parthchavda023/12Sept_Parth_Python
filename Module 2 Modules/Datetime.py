import datetime

sp=datetime.datetime.now()
print(sp)

print('\n')
print(sp.day)
print(sp.month)
print(sp.year)
print(f"Date:-{sp.day}/{sp.month}/{sp.year}")

print('\n')
print(sp.hour)
print(sp.minute)
print(sp.second)
print(sp.microsecond)
print(f"Time:-{sp.hour}:{sp.minute}:{sp.second}.{sp.microsecond}")