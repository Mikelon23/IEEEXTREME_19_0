import sys
import bisect
def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    q = int(data[1])
    arr = list(map(int, data[2:2+n]))
    idx = 2 + n
    results = []
    for i in range(q):
        x = int(data[idx])
        idx += 1
        first = bisect.bisect_left(arr, x)
        if first == n or arr[first] != x:
            results.append("-1 -1")
        else:
            last = bisect.bisect_right(arr, x) - 1
            results.append(f"{first + 1} {last + 1}")
    
    print("\n".join(results))
if __name__ == "__main__":
    main()