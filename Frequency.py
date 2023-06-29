def most_frequent(arr, Len):
    freq = {}
    for i in range(Len):
         
        if(arr[i] in freq):
            freq[arr[i]] = freq[arr[i]] + 1
        else:
            freq[arr[i]] = 1
    size = len(freq)
    while (size > 0):
        currentMax = 0
        arg_max = 0
        for key, value in freq.items():
            if (value > currentMax or (value == currentMax and key > arg_max)):
                arg_max = key
                currentMax = value
        print(f"{arg_max} = {currentMax}")
        freq.pop(arg_max)
        size -= 1
Str = input("Enter:")
Len = len(Str)
most_frequent(list(Str), Len)
