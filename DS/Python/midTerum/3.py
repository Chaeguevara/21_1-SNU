def insertion_sort(L: list) -> None:
    for i in range(1, len(L)):
        for j in range(i,0,-1): 
            if L[j-1] > L[j]:
                L[j-1], L[j] = L[j], L[j-1]
            else:
                break

l = [3,-1,10,-9]
insertion_sort(l)
print(l)