class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_hash , t_hash = {}, {}

        for c in s:
            s_hash[c] = s_hash.get(c, 0) + 1
        
        for c in t:
            t_hash[c] = t_hash.get(c, 0) + 1

        return t_hash == s_hash
        
