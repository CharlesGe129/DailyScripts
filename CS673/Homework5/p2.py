
content = "You can view your grades based on What-If scores so that you know how grades will be affected by upcoming or resubmitted assignments. You can test scores for an assignment that already includes a score, or an assignment that has yet to be graded."
aa = content.split(' ')
L = [len(each) for each in aa]
n = len(L)
M = 20

V = [-1 for i in range(n)]
N = [list() for i in range(n)]
V[n-1] = 0
N[n-1] = [1]
i = n-2
while i >= 0:
    a = aa[i]
    cur_length = L[i]
    j = i + 1
    if j < n:
        V[i] = (M - cur_length) ** 3 + V[j]
        N[i] = [j - i] + N[j]
    else:
        V[i] = (M - cur_length) ** 3
        N[i] = [j - i]
    while cur_length <= M:
        if j >= n:
            V[i] = 0
            N[i] = [j-i]
            break
        b = aa[j]
        cur_value = (M - cur_length)**3 + V[j]
        if cur_value < V[i]:
            V[i] = cur_value
            N[i] = [j-i] + N[j]
        cur_length += L[j] + 1
        j += 1
    i -= 1
optimal_value = V[0]
optimal_solution = N[0]
print(V)
print(N)
j = 0
for each in N[0]:
    i = each
    while i > 0:
        print(aa[j] + " ", end='')
        j += 1
        i -= 1
    print()
