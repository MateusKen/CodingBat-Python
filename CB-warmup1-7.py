'''
exercício: warmup-1 (pos-neg)
https://codingbat.com/prob/p162058
'''

def pos_neg(a, b, negative):
  if negative == True:
    if a<0 and b<0:
      return True
    else:
      return False
  elif (a<0 and b>0) or (a>0 and b<0):
    return True
  else:
    return False
