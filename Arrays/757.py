class Solution:
    def intersectionSizeTwo(self, intervals):
        # Sort by end ascending, start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # Track the last two chosen points
        p1 = -1
        p2 = -1
        ans = 0
        
        for start, end in intervals:
            # Case 1: no overlap with p1 or p2
            if start > p1:
                # add end-1 and end
                ans += 2
                p2 = end - 1
                p1 = end
            # Case 2: only 1 point overlaps
            elif start > p2:
                # add end
                ans += 1
                p2 = p1
                p1 = end
            # Case 3: already have 2 points overlapping → do nothing

        return ans
