#使用python内置的doctest来测试
def mul(a,b):
    """
    >>>mul(10,2)
    21
    >>>mul('y',2)
    yy
    """
    return a * b

def add(a,b):
    """
    >>>add(-1,-2)
    -3
    """

    return a + b

#测试乘法
