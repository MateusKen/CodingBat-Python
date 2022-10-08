'''
exercício: warmup-2 (string_splosion)
https://codingbat.com/prob/p118366
'''

def string_splosion(str):
    r = ''
    for i in range(len(str)+1):
        r += str[0:i]
    return r
