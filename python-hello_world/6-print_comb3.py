for i in range(10):
  for j in range(10):
    if i < j:
      if i == 8 and j == 9:
        print("{:01d}{:01d}".format(i, j))
      else:
        print("{:01d}{:01d}, ".format(i, j), end='')