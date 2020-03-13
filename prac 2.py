# explaining use of iterables and iterator
# oterables example
print("-----iterables----")
city = ["Mumbai", "Pune", "Delhi", "Patna"]
for i in city:
    print(i)

print("\n")

# iterator example
print("----iteraors----")

iterator_obj = iter(city)

try:
    print(next(iterator_obj))
    print(next(iterator_obj))
    print(next(iterator_obj))
    print(next(iterator_obj))
    print(next(iterator_obj))

except:
    print("stop iteration exception raised")
