if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newList=list(arr)
    newList.sort(reverse=True)
    first=newList[0]
    for num in newList:
        if num < first:
            print(num)
            break
            