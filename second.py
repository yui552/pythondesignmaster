def generator(max):
    print("generator created")
    n=0
    while n<max:
        x = yield n
        print('x={}'.format(x))
        print("yield called")
        n += 1
gen= generator(10)
a=next(gen)
a=next(gen)
a=next(gen)
a=next(gen)
a=next(gen)
print(a)
# for x in gen:
#     print('x={}'.format(x))


 

