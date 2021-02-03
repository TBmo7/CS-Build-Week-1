list_a = [44,5,9,6,4,44,69,79,888,-1,3,446,64]

def insertion(arr,n):
    if n==0:
        return
    insertion(arr,n-1)
    last = arr[n-1]
    j = n-2
    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j=j-1
    arr[j+1] = last

insertion(list_a,)
print(list_a)