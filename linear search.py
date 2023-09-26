def linear_search(arr,key):
    for i in range(len(arr)):
        if key==arr[i]:
            print("key element is found")
            break
    else:
        print("key is not found")

arr=[0,1,2,3,4,5,6,7,8,9]
key=int(input("Enter the search element:\n "))
linear_search(arr,key)




    
