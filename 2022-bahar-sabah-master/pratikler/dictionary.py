# from collections import defaultdict
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print(i)

# from collections import defaultdict

# # Inputs
# # ------
# n, m = map(int, input().split(' '))

# # Let's get the groups as lists
# # -----------------------------
# input1 = ['a', 'a', 'b', 'a', 'b']
# input2 = ['a', 'b']
# input1 = list()
# for i in range(n):
#     input1.append(input())

#     input2 = list()
# for i in range(m):
#     input2.append(input())

# # Calculate Output
# # ----------------
# d = defaultdict(list)

# # Fill d with input1 values
# for i in range(n):
#     d[input1[i]].append(i+1)
# #print(d) --> defaultdict(<class 'list'>, {'a': [1, 2, 4], 'b': [3, 5]})

# # Apply the logic for printing
# for i in input2:    
#     if i in d:
#         print(*d[i])
#     else:
#         print(-1)
# toplam=0
# x=5
# y=complex(x)
# for y in range(10):
#   toplam += toplam + 1