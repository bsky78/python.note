def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd();
print('执行第一次',next(o))
print('执行第二次',next(o))
print('执行第三次',next(o))    