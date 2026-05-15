import heapq
import sys


def main():
    input = sys.stdin.readline  # 200 iq move (запоминаем)

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    good = []
    bad = []

    for x, y in zip(a, b):
        if y >= x:
            good.append((x, y))
        else:
            bad.append((x, y))

    hearts = 1
    ans = 0

    good.sort()

    for cost, inside in good:
        if hearts >= cost:
            hearts += inside - cost
            ans += 1
        else:
            break

    bad.sort(key=lambda item: item[1], reverse=True)

    total_loss = 0
    heap = []

    for cost, inside in bad:
        loss = cost - inside

        total_loss += loss
        heapq.heappush(heap, -loss)

        if total_loss > hearts - inside:
            removed = -heapq.heappop(heap)
            total_loss -= removed

    ans += len(heap)

    print(ans)


if __name__ == "__main__":
    main()
