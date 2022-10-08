'''
exercício: warmup-2 (array_front9)
https://codingbat.com/prob/p110166
'''

def array_front9(nums):
    for i in range(len(nums)):
        if nums[i] == 9 and i<4:
            return True
    return False
