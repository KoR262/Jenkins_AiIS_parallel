from sys import argv
arg = argv[2]

def test1():
    if (arg == "Test1") or (arg == "Test2") or (arg == "Test3"):
        assert True
    else:
        assert False

def test2():
    if (arg == "Test1") or (arg == "Test2"):
        assert True
    else:
        assert False

def test3():
    if (arg == "Test1"):
        assert True
    else:
        assert False