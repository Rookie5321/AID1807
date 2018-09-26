from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()
    print(34)


def test2():
    print("ab")
    gr1.switch()
    print("cd")


# 协程对象
gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()



















