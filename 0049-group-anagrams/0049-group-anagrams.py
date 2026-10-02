class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        help = []

        for i in range(len(strs)):
            a = ''.join(sorted(strs[i]))
            help.append(a)

        ans = []

        for i in range(len(help)):
            already_present = False
            for group in ans:
                if strs[i] in group:
                    already_present = True
                    break

            if already_present:
                continue

           
            group = [strs[i]]

            for j in range(i + 1, len(help)):
                if help[i] == help[j]:
                    group.append(strs[j])

            ans.append(group)

        return ans