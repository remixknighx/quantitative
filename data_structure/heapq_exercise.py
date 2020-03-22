# -*- coding: utf-8 -*-
"""
reference https://www.jianshu.com/p/801318c77ab5
"""
import heapq

if __name__ == '__main__':
    nums = [2, 3, 5, 1, 54, 23, 132]
    heap = []
    for num in nums:
        heapq.heappush(heap, num)  # 加入堆

    print(heap[0])  # 如果只是想获取最小值而不是弹出，使用heap[0]
    print(heap)
    print([heapq.heappop(heap) for _ in range(len(nums))])  # 堆排序结果

    # 第二种
    # nums = [2, 3, 5, 1, 54, 23, 132]
    # heapq.heapify(nums)
    # print([heapq.heappop(heap) for _ in range(len(nums))])  # 堆排序结果
    # out: [1, 2, 3, 5, 23, 54, 132]