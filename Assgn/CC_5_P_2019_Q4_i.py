lst = [2.0, -1.2, 3.4, 9.1, 0.1, -5.8, -4.2, 3.9, 10.4, 1.9, -3.8, -9.6]

sublst = lst[4:9] #taking index 4 to 8 (both included)

res = sum(sublst) > sum(lst)

print("Sum of the SLICED List is GREATER THAN sum of List: ", res)
