array = [1,2,8,3,8,6,7,8,8,9]
count=0
target=8
while target in array :
  
    array.remove(target)
    array.append(0)
    count+=1
# while left <= right:
#     if array[left] == target:
#         array[left] = array[right]
#         array[right] = 0
#         right -= 1
#         count += 1
#     else:
#         left += 1

print(len(array) - count)
print(array)