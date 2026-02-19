import numpy as np
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s:
            return 0
        arr = np.array(list(s), dtype=int)
        changes = np.where(np.diff(arr) != 0)[0]
        boundaries = np.concatenate(([-1], changes, [len(arr) - 1]))
        group_lengths = np.diff(boundaries)
        return int(np.sum(np.minimum(group_lengths[:-1], group_lengths[1:])))