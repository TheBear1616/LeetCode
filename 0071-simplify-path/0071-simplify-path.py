class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirName = ""
        path += "/"

        for char in path:
            if char == "/" and len(dirName) > 0:
                if dirName == "..":
                    if stack: stack.pop()
                elif dirName != ".":
                    stack.append(dirName)
                dirName = ""
            elif char != "/":
                dirName += char
        
        return "/" + "/".join(stack)