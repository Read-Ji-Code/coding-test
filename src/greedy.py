def coin_split(total_value=0):
    count = 0
    coin_types = [500, 100, 50, 10]

    for coin in coin_types:
        count = count + (total_value // coin)
        total_value = total_value % coin

    return count

def law_of_large_numbers(p1, p2):
    _, m, k = p1

    p2.sort()
    first =  p2[-1]
    second = p2[-2]
    result = 0
    print(first, second)
    
    #계산

    while True :
        for i in range(k):
           result = result + first
           m = m -1
        result = result + second   
        m = m - 1   
        if m == 0 :
              break
        
    return reslut
           
if __name__ == "__main__":
    law_of_large_numbers((5, 8, 3), (1, 2, 3, 4, 5))