class Solution:
    def simplifyPath(self, path: str) -> str:
        curpath = []
        path = path.split("/")
        for elem in path:
            if curpath and elem == "..": curpath.pop()
            elif elem not in [".", "", ".."]: curpath.append(elem)
        return "/" + "/".join(curpath) 