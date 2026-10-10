class Solution:
    def minSumSquareDiff(
        self, nums1: List[int], nums2: List[int], k1: int, k2: int
    ) -> int:
        differences = [abs(a - b) for a, b in zip(nums1, nums2)]
        total_operations = k1 + k2

        if sum(differences) <= total_operations:
            return 0

        max_diff = max(differences)

        def feasible(target):
            return sum(max(diff - target, 0) for diff in differences) <= total_operations

        left, right = 0, max_diff - 1
        first_true_index = max_diff

        while left <= right:
            mid = (left + right) // 2

            if feasible(mid):
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1

        optimal_threshold = first_true_index

        for i, diff in enumerate(differences):
            operations_used = max(0, diff - optimal_threshold)
            differences[i] = min(optimal_threshold, diff)
            total_operations -= operations_used

        for i, diff in enumerate(differences):
            if total_operations == 0:
                break

            if diff == optimal_threshold:
                total_operations -= 1
                differences[i] -= 1

        return sum(diff * diff for diff in differences)