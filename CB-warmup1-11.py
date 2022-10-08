'''
exercício: warmup-1 (front3)
https://codingbat.com/prob/p147920
'''

def front3(str):
  if len(str)<=1:
    return 3*str
  elif len(str)<=2:
    return 3*str[0:2]
  else:
    return 3*str[0:3]
