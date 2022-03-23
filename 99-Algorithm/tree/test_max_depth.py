from collections import deque
from prac import make_tree_by
testlist = [3, 9, 20, 4, 12, 15, 7]
def test_max_depth(lst):
    root = make_tree_by(lst, 0)
    
    if not root:
        return 0
    q = deque([root])
    depth = 0
    
    while q:
        print(f'while start ---------')
        depth += 1
        print(f'depth ++ depth is {depth}')
        for _ in range(len(q)):
            print(f'for start ----------------')
            #print(f'_ is {_}\n q is {q}\n length is {len(q)}')
            cur = q.popleft()
            print(f'cur is {cur.val}\n i is {_}')
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            print(f'q is {len(q)}')
            print(f'for end------------------')
        print(f'while end -------- q is {len(q)}\n')

    return depth

test_max_depth(testlist)
