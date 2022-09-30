# A: Glory Addicts -> timeout error on test 4
def get_score(a, b, idx_map):
    score = 0
    idx = idx_map[0]
    score = b[idx]
    for i in range(1, len(a)):
        idx = idx_map[i]
        if a[idx_map[i - 1]] != a[idx]:
            score += (2 * b[idx])
        else:
            score += b[idx]
    return score
 
if __name__ == '__main__':
    skills = int(input())
    for i in range(skills):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        zset, oset = [], []
        for j in range(len(a)):
            if a[j] == 1:
                oset.append((b[j], j))
            else:
                zset.append((b[j], j))
        
        idx_map = [0] * len(a)
        idx = 0
        while oset or zset:
            set_to_add = None
            if idx > 0 and a[idx_map[idx - 1]] == 1 and zset:
                set_to_add = max(zset)
            elif idx > 0 and a[idx_map[idx - 1]] != 1 and oset:
                set_to_add = max(oset)
            else:
                if len(oset) > len(zset):
                    set_to_add = min(oset)
                elif len(oset) < len(zset):
                    set_to_add = min(zset)
                else:
                    set_to_add = min( min(oset), min(zset) )
 
            if set_to_add in oset:
                oset.remove(set_to_add)
            if set_to_add in zset:
                zset.remove(set_to_add)
 
            idx_map[idx] = set_to_add[1]
            idx += 1
        print(get_score(a, b, idx_map))


# A: Glory Addicts -> memory error on test 4, makes sense because of so many permutations
from itertools import permutations
def get_score(a, b, idx_map):
    score = 0
    idx = idx_map[0]
    score = b[idx]
    for i in range(1, len(a)):
        idx = idx_map[i]
        if a[idx_map[i - 1]] != a[idx]:
            score += (2 * b[idx])
        else:
            score += b[idx]
    return score
 
if __name__ == '__main__':
    skills = int(input())
    for i in range(skills):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
 
        indexes = []
        for i in range(len(a)):
            indexes.append(i)
        perms = list(permutations(indexes))
 
        m_score = 0
        for i in range(len(perms)):
            m_score = max(m_score, get_score(a, b, perms[i]))
        print(m_score)