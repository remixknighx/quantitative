# -*- coding: utf-8 -*-
"""
811. Subdomain Visit Count
@link https://leetcode.com/problems/subdomain-visit-count/
"""
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result = []
        result_dict = dict()
        for cpdomain in cpdomains:
            count = int(cpdomain.split(" ")[0])
            domain = cpdomain.split(" ")[1]
            sub_domains = domain.split(".")
            sub_domain = ''
            for sub in sub_domains[::-1]:
                sub_domain = sub + "." + sub_domain
                if result_dict.get(sub_domain) is None:
                    result_dict[sub_domain] = count
                else:
                    new_count = result_dict.get(sub_domain) + count
                    result_dict[sub_domain] = new_count

        for key in result_dict.keys():
            result.append(str(result_dict.get(key)) + " " + key[:-1])

        return result


if __name__ == '__main__':
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print(Solution().subdomainVisits(cpdomains=cpdomains))
