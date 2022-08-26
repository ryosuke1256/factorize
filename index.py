  1 def factorize(num):
  2     if num <= 1: return 1  
  3     return num * factorize(num - 1)
  4 n = input('数値を入力してください:')
  5 print(str(n) + 'の階乗は' + str(factorize(int(n))))
