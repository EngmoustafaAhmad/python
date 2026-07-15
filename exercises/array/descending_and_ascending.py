arr = []
for n in range(5):
  
  i = int(input("enter numbers"))
  arr.append(i)
print(arr)
print("descending array")
arr.sort(reverse=True)
print(arr)
print("ascending array")
arr.sort()
print(arr)
