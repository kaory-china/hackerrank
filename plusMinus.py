def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    len_arr = len(arr)
    
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        elif i == 0:
            zero += 1

        positive_ratio = positive/len_arr
        negative_ratio = negative/len_arr 
        zero_ratio = zero/len_arr
    
    print('{:.6f}\n{:.6f}\n{:.6f}'.format(positive_ratio, negative_ratio, zero_ratio))

arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)