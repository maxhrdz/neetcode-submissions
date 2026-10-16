class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

    
        output = {}
        
        for i in strs:
            sorteds = ''.join(sorted(i))
            if sorteds in output:
                output[sorteds].append(i)
            else:
                output[sorteds] = [i]

        return list(output.values())

        