# -*- coding: utf-8 -*-

"""
690. Employee Importance
@link https://leetcode.com/problems/employee-importance/
"""
from typing import List

class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, id: int) -> int:
        e_dict = {}
        for employee in employees:
            e_dict[employee.id] = employee
        return self.bfs(employee=e_dict[id], e_dict=e_dict)

    def dfs(self, employee: Employee, e_dict: dict):
        count: int = employee.importance
        for sub_employee in employee.subordinates:
            count += self.dfs(employee=e_dict[sub_employee], e_dict=e_dict)
        return count

    def bfs(self, employee: Employee, e_dict: dict):
        count: int = 0
        e_queue = []
        e_queue.append(employee.id)
        while e_queue:
            employee_id = e_queue.pop(0)
            count += e_dict[employee_id].importance
            e_queue.extend(e_dict[employee_id].subordinates)
        return count


if __name__ == '__main__':
    employee_2 = Employee(2, 3, [4])
    employee_3 = Employee(3, 4, [])
    employee_4 = Employee(4, 1, [])
    employee_1 = Employee(1, 5, [2, 3])
    print(Solution().getImportance(employees=[employee_1, employee_2, employee_3, employee_4], id=1))
