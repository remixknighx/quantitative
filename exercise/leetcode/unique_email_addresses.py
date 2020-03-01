# -*- coding: utf-8 -*-
"""
929. Unique Email Addresses
@link https://leetcode.com/problems/unique-email-addresses/
"""
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            local_name = email.split('@')[0].split('+')[0].replace('.','')
            domain = email.split('@')[1]
            email_set.add(local_name + '@' + domain)
        return len(email_set)


if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    print(Solution().numUniqueEmails(emails=emails))
