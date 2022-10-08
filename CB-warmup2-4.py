'''
exercício: warmup-2 (array_count9)
https://codingbat.com/prob/p166170
'''

def array_count9(nums):
    cont = 0
    for i in range(len(nums)):
        if nums[i] % 9 ==0:
            cont += 1
    return cont
