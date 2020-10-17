from itertools import permutations
from more_itertools import windowed 
def is_seq_sorted(lst):
  print(lst)  
  return all(
    x <= y
    for x, y in windowed(lst, 2)
  )
def permutation_sort(lst):
  return next(
    permutation_seq
    for permutation_seq in permutations(lst)
    if is_seq_sorted(permutation_seq)
  )
print("All the sequences:")
print("\nSorted sequence: ",permutation_sort([12, 10, 9]))

print("\n\nAll the sequences:")
print("\nSorted sequence: ",permutation_sort([2, 3, 1, 0]))
