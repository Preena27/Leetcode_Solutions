class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left_count = moves.count("L")
        right_count = moves.count("R")
        wildcard_count = moves.count("_")
        furthest_distance = abs(left_count - right_count) + wildcard_count
        return furthest_distance

        