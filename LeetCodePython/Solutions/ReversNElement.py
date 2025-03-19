# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 3

# for i in range(0, len(lst), target):
  
#     lst[i:i+target] = reversed(lst[i:i+target])
#print(lst)




array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("Enter the value of n: "))
length = len(array)
    
for i in range(0, length, n):
        left = i
        right = min(i + n - 1, length - 1)  
        
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
print(result)