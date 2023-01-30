import random
def main():
  num = int(input("Pick a Number between 0 and 20: "))
  S = random.randrange(0,20)
  
  
  if num == S:
    print("player number", num)
    print("Correct number", S)
    print("Good Job")
  else:
    print("player number", num)
    print("Correct number", S)
    print("too bad")
if __name__ == "__main__":
  main()