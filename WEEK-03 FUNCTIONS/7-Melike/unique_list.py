################### 1. unique_list ############

def unique_list(*args):

    my_set = set(args)
    my_list = [*my_set]
    print(my_list)
args = input("please enter your nums: ")
unique_list(*args)
