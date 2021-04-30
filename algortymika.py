import time
import random
import math

def insertion_sort(A):
    for j in range(1,len(A)):
        card = A[j]
        i = j - 1
        while i >= 0 and A[i] > card:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = card
    return f'INSERTION SORT - {A}'

def bubble_sort(A):
    n = len(A) - 1
    while n >= 1:
        w = 1
        for j in range(0, n):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                w = j
            n = w - 1
    return f'BUBBLE SORT - {A}'

def merge(A,B):
    i = 0
    j = 0
    C = []
    while i <= n and j <= m:
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    while i <= n:
        C.append(A[i])
        i += 1
    while j<= 1:
        C.append(B[j])
        j += 1
    return f'MERGE - {C}'

def merge_sort(A):                      # sth in this part does not work
    n = int(len(A) + 1)
    if n > 0:
        q = math.floor(n/2)
        merge_sort(A[:q])
        merge_sort(A[q:n])
        merge(A[:q],A[q:n])
    return f'MERGE SORT - {A}'

def insertion_time(A):
    start = time.time_ns()
    outcome = insertion_sort(A)
    stop = time.time_ns()
    da_time = stop - start
    return f'INSERTION SORT: time needed (in ns): {da_time}'

def bubble_time(A):
    start = time.time_ns()
    outcome = bubble_sort(A)
    stop = time.time_ns()
    da_time = stop - start
    return f'BUBBLE SORT: time needed (in ns): {da_time}'

def sort_time(A):
    start = time.time_ns()
    testlist.sort()
    stop = time.time_ns()
    da_time = stop - start
    return f'BUILT-IN SORT: time needed (in ns): {da_time}'

def merge_time(A):
    start = time.time_ns()
    outcome = merge_sort(A)
    stop = time.time_ns()
    da_time = stop - start
    return f'MERGE SORT: time needed (in ns): {da_time}'


testlist = []
list_len = int(input('List lenght: '))
for i in range(list_len):
    testlist.append(random.randint(0,1000000))


print(merge_sort(testlist))

print(insertion_time(testlist))
print(bubble_time(testlist))
print(sort_time(testlist))
