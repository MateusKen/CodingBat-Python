'''
exercício: warmup-1 (missing_char)
https://codingbat.com/prob/p149524
'''

def missing_char(str, n):
  Str = ''
  for i in range(len(str)):
    if i != n:
      Str += str[i]
  return Str
