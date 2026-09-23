class SegmentTreeNode:
    def __init__(self, k: int):
        self.prod = 1
        self.remain = [0] * k

class SegmentTree:
    def __init__(self, nums: list[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree = [SegmentTreeNode(k) for _ in range(4 * self.n)]
        self._build(nums, 0, 0, self.n - 1)

    def _merge(self, left: SegmentTreeNode, right: SegmentTreeNode) -> SegmentTreeNode:
        parent = SegmentTreeNode(self.k)
        parent.prod = (left.prod * right.prod) % self.k
        
        # Prefixes ending in the left segment keep their remainders
        for r in range(self.k):
            parent.remain[r] += left.remain[r]
            
        # Prefixes ending in the right segment are multiplied by the product of the left segment
        for r in range(self.k):
            next_r = (r * left.prod) % self.k
            parent.remain[next_r] += right.remain[r]
            
        return parent

    def _build(self, nums: list[int], node: int, start: int, end: int):
        if start == end:
            val = nums[start] % self.k
            self.tree[node].prod = val
            self.tree[node].remain[val] = 1
            return

        mid = (start + end) // range(2)[1] # safe mid calculation
        mid = (start + end) // 2
        self._build(nums, 2 * node + 1, start, mid)
        self._build(nums, 2 * node + 2, mid + 1, end)
        self.tree[node] = self._merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, node: int, start: int, end: int, idx: int, val: int):
        if start == end:
            v = val % self.k
            self.tree[node].remain = [0] * self.k
            self.tree[node].prod = v
            self.tree[node].remain[v] = 1
            return

        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node + 1, start, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, val)
        self.tree[node] = self._merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, node: int, start: int, end: int, l: int, r: int) -> SegmentTreeNode:
        if l <= start and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        if r <= mid:
            return self.query(2 * node + 1, start, mid, l, r)
        if l > mid:
            return self.query(2 * node + 2, mid + 1, end, l, r)

        left_res = self.query(2 * node + 1, start, mid, l, r)
        right_res = self.query(2 * node + 2, mid + 1, end, l, r)
        return self._merge(left_res, right_res)


class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        st = SegmentTree(nums, k)
        ans = []
        
        for idx, val, start, xi in queries:
            # 1. Apply persistent point update
            st.update(0, 0, n - 1, idx, val)
            
            # 2. Query the active suffix range from start to n-1
            res_node = st.query(0, 0, n - 1, start, n - 1)
            
            # 3. Collect the precalculated combinations that match xi
            ans.append(res_node.remain[xi])
            
        return ans