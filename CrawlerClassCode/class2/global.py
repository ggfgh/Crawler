a = 10
def test():
        global a
        a = 5
        print(a)
test()
print(a)
a = 20
print(a)