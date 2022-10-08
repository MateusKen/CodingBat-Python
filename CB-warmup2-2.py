'''
exercício: warmup-2 (front_times)
https://codingbat.com/prob/p165097
'''

#solução sem loop
def front_times(str, n):
    if len(str)<2:
        return n*str
    elif len(str)<3:
        return n*str[0:2]
    else: 
        return n*str[0:3]
        
#com loop
def front_times(str, n):
  terc = 3
  if terc > len(str):
    terc = len(str)
  f = str[:terc]
  
  r = ""
  for i in range(n):
    r += f
  return r
