def solution(num, total):
    ans = []

    if num % 2 == 0:
        lt, rt = (total//num), (total//num)+1
        ans.append(lt)
        ans.append(rt)
        for i in range(1, (num)//2):
            ans.append(lt-i)
            ans.append(rt+i)
    else:
        mid = (total//num)
        ans.append(mid)
        for i in range(1, (num-1)//2+1):
            ans.append(mid+i)
            ans.append(mid-i)

    return sorted(ans)
