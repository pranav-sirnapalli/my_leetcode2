class Solution:
    def longestDupSubstring(self, s: str) -> str:
        p = 2 ** 63 - 1
        # Rabin karp algorithm to find duplicate string
        def rabin_karp(mid):
            cur_hash = 0
            for i in range(mid):
                cur_hash = (cur_hash * 26 + nums[i]) % p
            hashes = {cur_hash}
            pos = -1
            max_pow = pow(26, mid, p)

            for i in range(mid, len(s)):
                cur_hash = (26 * cur_hash-nums[i-mid]*max_pow+nums[i]) % p
                if(cur_hash in hashes):
                    pos = 1 + i - mid
                hashes.add(cur_hash)
            return pos


        # Binary search to find midpoint
        nums = [ord(c) for c in s]
        l, r = 0, len(s)-1
        
        while(l<=r):
            mid = (l + r) // 2
            pos = rabin_karp(mid)
            if(pos == -1):
                r = mid - 1
            else:
                start, end = pos, pos+mid
                l = mid + 1
        
        return s[start:start+l-1]
    