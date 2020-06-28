#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-06-28 10:14:36
@LastEditor: John
@LastEditTime: 2020-06-28 10:19:25
@Discription: 
@Environment: python 3.7.7
'''
#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """广度优先搜索
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque() # 使用队列先进先出
        queue.append(root)
        res = []
        i=0
        while queue:
            size = len(queue)
            level = [] # 对应深度的所有值
            i+=1
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                ## 加上深度奇偶判断
                if i%2==1:
                    level.append(cur.val)
                else:
                    level.insert(0,cur.val) # 也可以appendleft
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res
# @lc code=end

