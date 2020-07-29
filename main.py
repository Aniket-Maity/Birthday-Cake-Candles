def birthdayCakeCandles(ar):
    maxEle = max(ar)
    count = 0
    for element in ar:
        if(maxEle==element):
            count+=1
    return count
if __name__ == '__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))
    print(birthdayCakeCandles(ar))