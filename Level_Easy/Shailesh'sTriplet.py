import sys
def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        N = int(data[index])
        index += 1
        if N % 2 != 0:
            results.append("-1")
        else:
            if N & (N - 1) == 0:
                results.append("-1")
            else:
                d = 1
                while d * 2 <= N:
                    d <<= 1
                K = N // 2
                A = K | d
                B = K
                C = N - d
                results.append(f"{A} {B} {C}")
    print("\n".join(results))
if __name__ == "__main__":
    main()