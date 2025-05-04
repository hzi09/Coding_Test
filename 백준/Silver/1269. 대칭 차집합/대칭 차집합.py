a, b = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_set = set(a_list)
b_set = set(b_list)

symmetric_difference = a_set ^ b_set

print(len(symmetric_difference))