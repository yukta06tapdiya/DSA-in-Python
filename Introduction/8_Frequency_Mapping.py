#frequency mapping:
#method1
def frequency_mapping(arr):
    freq_map={}
    for i in range(0,len(arr)): #O(n)
        if arr[i] in freq_map: #O(1)
            freq_map[arr[i]]+=1 #O(1)
        else:
            freq_map[arr[i]]=1 #O(1)
    return (freq_map)

#method2
def hashing_mapping(arr):
    hash_map={}
    for i in range(0,len(arr)):
        hash_map[arr[i]]=hash_map.get(arr[i],0)+1
    return (hash_map)

list=[1,2,7,2,5,9,5,6,6]
a=frequency_mapping(list)
print(a)
b=hashing_mapping(list)
print(b)