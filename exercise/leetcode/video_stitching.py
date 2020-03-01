# -*- coding: utf-8 -*-
"""
1024. Video Stitching
@link https://leetcode.com/problems/video-stitching/
"""
from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        count = 0
        reach = -1 # the end time of the previously selected clip
        nextReach = 0
        for i in range(0, len(clips)):
            clip = clips[i]
            if clip[0] > reach:
                if clip[0] > nextReach:
                    return -1
                reach = nextReach
                count += 1

            nextReach = max(nextReach, clip[1])
            if nextReach >= T:
                break

        return -1 if nextReach < T else count


if __name__ == '__main__':
    clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
    print(Solution().videoStitching(clips=clips, T=10))
