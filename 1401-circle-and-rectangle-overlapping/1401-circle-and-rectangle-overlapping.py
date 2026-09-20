class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def get_closest_distance_to_range(range_start, range_end, point):
            if range_start <= point <= range_end:
                return 0
            if point < range_start:
                return range_start - point
            return point - range_end

        horizontal_distance = get_closest_distance_to_range(x1, x2, xCenter)
        vertical_distance = get_closest_distance_to_range(y1, y2, yCenter)

        squared_distance = horizontal_distance ** 2 + vertical_distance ** 2
        squared_radius = radius ** 2

        return squared_distance <= squared_radius