def sum_all(*args):
    print(*args)
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3))
# print(sum_all([1,2,3]))


# if we dont use * before args, then it povide the value in tuples and we can see that by printing args and *args