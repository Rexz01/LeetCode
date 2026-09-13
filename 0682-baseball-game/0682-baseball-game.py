class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if not operations:
            return -1

        num = []

        for op in operations:

            if op == "C":
                if not num:
                    return -1
                num.pop()

            elif op == "D":
                if not num:
                    return -1
                num.append(2 * num[-1])

            elif op == "+":
                if len(num) < 2:
                    return -1
                num.append(num[-1] + num[-2])

            else:
                num.append(int(op))

        return sum(num)