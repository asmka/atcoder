import queue

def main():
    K = int(input())

    numq = queue.Queue()
    for n in range(1, 9+1):
        numq.put(n)

    ans = None
    for _ in range(K):
        n = numq.get()
        #print('[DEBUG] n: ', n)
        #print('[DEBUG] type(n): ', type(n))
        base = n*10
        if base//10%10 >= 1:
            numq.put(base + (base//10%10-1))
        numq.put(base + (base//10%10))
        if base//10%10 <= 8:
            numq.put(base + (base//10%10+1))
        ans = n

    print(ans)
        

if __name__=='__main__':
    main()
