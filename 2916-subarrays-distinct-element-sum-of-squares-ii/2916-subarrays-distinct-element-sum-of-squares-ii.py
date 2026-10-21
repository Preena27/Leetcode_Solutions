class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        size = 4 * n

        total = [0] * size
        squares = [0] * size
        lazy = [0] * size

        def apply(node: int, left: int, right: int, value: int) -> None:
            length = right - left + 1
            squares[node] = (
                squares[node] + 2 * value * total[node] + value * value * length
            ) % mod
            total[node] = (total[node] + value * length) % mod
            lazy[node] = (lazy[node] + value) % mod

        def push(node: int, left: int, right: int) -> None:
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            apply(node * 2, left, mid, lazy[node])
            apply(node * 2 + 1, mid + 1, right, lazy[node])
            lazy[node] = 0

        def add(node: int, left: int, right: int, ql: int, qr: int) -> None:
            if ql <= left and right <= qr:
                apply(node, left, right, 1)
                return

            push(node, left, right)
            mid = (left + right) // 2

            if ql <= mid:
                add(node * 2, left, mid, ql, qr)
            if qr > mid:
                add(node * 2 + 1, mid + 1, right, ql, qr)

            total[node] = (total[node * 2] + total[node * 2 + 1]) % mod
            squares[node] = (squares[node * 2] + squares[node * 2 + 1]) % mod

        last_seen = {}
        answer = 0

        for i, value in enumerate(nums):
            previous = last_seen.get(value, -1)
            add(1, 0, n - 1, previous + 1, i)
            last_seen[value] = i
            answer = (answer + squares[1]) % mod

        return answer
