'''
exercício: warmup-1 (front_back)
https://codingbat.com/prob/p153599
'''

#minha solução
def front_back(str):
  r = ''
  t = len(str)-1
  if t <=0:
    return str
  else:
    r += str[t]
    for i in range(1, t):
      r +=str[i]
    r += str[0]
    return r
  
#solução deles
def front_back(str):
  if len(str) <=1:
    return str
  else:
    meio = str[1:-1]
    return str[len(str)-1]+meio+str[0]
