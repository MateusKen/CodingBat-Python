'''
exercício: warmup-1 (parrot_trouble)
https://codingbat.com/prob/p166884
'''

def parrot_trouble(talking, hour):
  if talking == False:
    return False
  else:
    if hour <7 or hour>20:
      return True
    else:
      return False
      
