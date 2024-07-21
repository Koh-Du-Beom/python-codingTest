import sys
input = sys.stdin.readline



while True:
  question = input()
  if question == 0:
    break
  
  num_list = list(map(int, question.split()))
  numbers = num_list[1:]
  
  print(numbers)
  
  
  


  
  
  
  