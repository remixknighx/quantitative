# -*- coding: utf-8 -*-
"""
1108. Defanging an IP Address
@link https://leetcode.com/problems/defanging-an-ip-address/
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


if __name__ == '__main__':
    print(Solution().defangIPaddr(address='255.100.50.0'))