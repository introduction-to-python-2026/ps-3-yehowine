my_list = [0,0,0,0,1]
def move(my_list,direction = None):
  index_of_one=my_list.index(1)
  if direction == "right" and index_of_one != len(my_list) - 1:
    my_list[index_of_one] = 0 
    my_list[index_of_one + 1] = 1
  elif direction == "left" and index_of_one != 0:
    my_list[index_of_one] = 0
    my_list[index_of_one - 1] = 1
  elif direction is None:
    print("no direction, list remains unchanged")
  elif direction not in ["right", "left"]:
    print("error")
  return my_list
print(move(my_list, direction=None))
