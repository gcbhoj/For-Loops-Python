'''counting in 2D array HOURGlass'''

max_sum = float('-inf')
for i in range(4):
    for j in range(4):
        curent_sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]

        max_sum = max(max_sum, curent_sum)
return max_sum