class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = []
        for idx, token in enumerate(tokens):
            if token.lstrip("-").isdigit():
                operation.append(int(token))
            else:
                opTwo = operation.pop()
                opOne = operation.pop()
                if token == '/':
                    operation.append(int(opOne / opTwo))
                elif token == '*':
                    operation.append(int(opOne * opTwo))
                elif token == '+':
                    operation.append(int(opOne + opTwo))
                elif token == '-':
                    operation.append(int(opOne - opTwo))

        
        return operation[-1]