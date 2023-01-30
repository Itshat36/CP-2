def main():
  eggs = int(input("Enter number of eggs: "))
  price = 0.0
  cost = 0.0

  if eggs > 0 and eggs <=3:
    price = 0.5
  elif eggs > 3 and eggs <=5:
    price = 0.45
  elif eggs > 5 and eggs <=10:
    price = 0.4
  elif eggs >=11:
    price = 0.35

  cost = price * eggs
  print("price per eggs is $" + str(price))
  print("Total cost is $" + str(round(cost, 2)))
  pass


if __name__ == "__main__":
  main()