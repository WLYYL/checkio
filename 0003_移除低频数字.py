
import string

def checkio(data):
    '''
    我的方法
    list 在遍历过程中如果发生变化会导致遍历和预期不一样
    '''
    datacopy=data.copy()
    for v in datacopy:
        if datacopy.count(v) == 1:
            data.remove(v)
    return data
    
    # 简单方法
    # return [x for x in data if data.count(x) > 1]


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")