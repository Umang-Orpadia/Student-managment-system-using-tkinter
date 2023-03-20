def sum_is(arr):
    result=sum(arr)
    return result
if __name__=="__main__":
    arr=list(map(int, input("Enter multiple values: "). split()))
    print('sum_is: {}'.format(sum_is(arr)))
