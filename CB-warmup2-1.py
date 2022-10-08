'''
exercício: warmup-2 (string_times)
https://codingbat.com/prob/p193507
'''
#solução sem loop
def string_times(str, n):
    return n*str
  
#com loop
def string_times(str, n):
  r = ''
  for i in range(n):
    r+=str
  return r
