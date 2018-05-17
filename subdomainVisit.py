class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res = []
        domain_counter = collections.Counter()
        for item in cpdomains:
            domain_name = item.split(' ')[1]
            access_times = item.split(' ')[0]
            domain_name = domain_name.split('.')
            for i in range(len(domain_name)):
                domain_counter['.'.join(domain_name[i:len(domain_name)])] += int(access_times)
        # print(domain_counter)
        for key, value in domain_counter.items():
            res.append(' '.join((str(value), key)))
        return res
