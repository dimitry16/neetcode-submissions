class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = defaultdict(list)
        results = []

        for word in strs:
            barCode = [0] * 26
            for char in word:
                barCode [ord(char) - ord("a")] += 1
            wordDict[tuple(barCode)].append(word)

        for values in wordDict.values():
            results.append(values)
        return results

