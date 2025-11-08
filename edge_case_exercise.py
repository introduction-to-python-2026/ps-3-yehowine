def move(my_list, direction=None):

        index_of_one = my_list.index(1)
    except ValueError:
        print("Error: The integer 1 was not found in the list.")
        return my_list

    if direction == "right" and index_of_one != len(my_list) - 1:
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1
        
    elif direction == "left" and index_of_one != 0:
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1

    elif direction is None:
        print("No direction specified; list remains unchanged.")
        
    elif direction not in ["right", "left"]:
        print(f"Error: Invalid direction '{direction}'. List remains unchanged.")
        
    return my_list
