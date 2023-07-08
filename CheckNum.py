#Check if the first and last number of a list is the same
def checknum(list):
  if list[0] == list[-1]:
    return True
  else:
    return False

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
print(checknum(numbers_x))
print(checknum(numbers_y))