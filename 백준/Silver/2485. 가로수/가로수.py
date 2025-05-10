n = int(input())
tree = [int(input()) for _ in range(n)]

tree_diff = []
for i in range(1, n):
    tree_diff.append(tree[i] - tree[i-1])

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

g = tree_diff[0]
for diff in tree_diff[1:]:
    g = gcd(g, diff)

total_trees = (tree[-1] - tree[0]) // g + 1
answer = total_trees - n

print(answer)