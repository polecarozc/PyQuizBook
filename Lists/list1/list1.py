from xml.dom.expatbuilder import parseString


## Think SLICING for many of these.

def create_list_from_tuple(t):
    """
    This function takes a tuple of elements and returns a list containing those elements of the tuple.
    """
    return list(t)
    
def drop_last(lst):
    """
    This function takes a list and returns a list with the last item removed.
    """
    return lst[:-1]


def drop_first_two(lst):
    """
    This function takes a list and returns a list with the first two items removed.
    """
    return lst[2:]

def drop_mangle(lst):
    """
    This function takes a list and returns a list with the first two items AND last item removed.
    """
    return lst[2:-1]

def add_item_front(lst, a):
    """
    This function takes a list and an item,
    returning the list with the item prepended to the list
    """

    return [a] + lst

def add_item_end(lst, a):
    """
    This function takes a list and an item,
    returning the list with the item appended to the list
    """
    return lst + [a]

def add_list_to_list(lsta, lstb):
    """
    This function takes two lists and appends one to the other,
    returning a list
    """
    return lsta + lstb

def list_and_list_to_tuple(lsta, lstb):
    """
    This function takes two lists and returns a tuple containing the two lists
    """
    return lsta, lstb

def list_and_list_to_list(lsta, lstb):
    """
    This function takes two lists and returns a list containing the two lists
    """
    return list([lsta, lstb])

##
##
##

def list_from_range(n):
    """
    This function returns list with 0..n as integers in a list
    """
    return list(range(n))

def list_from_range2(n, m):
    """
    This function returns list with n..m (without m) as integers in a list
    """
    return list(range(n, m))

def list_from_range3(n, m):
    """
    This function returns list with n..m (including m(!)) as integers in a list
    """
    return list(range(n, m + 1))

def list_from_range4(n, m):
    """
    This function returns list with n..m (WITHOUT n and including m) as integers in a list
    """
    return list(range(n + 1, m + 1))

def list_from_range_by(n, step):
    """
    This function returns list with 0..n as integers by step in a list
    (read the test)
    """
    return list(range(0, n, step))

def rev_list(lst):
    """
    This function returns list which is a reverse of the argument list
    (read the test)
    """
    return list(lst[::-1])
  
def concat_list_indexwise(lst1, lst2):
    """
    Write a program to add two lists index-wise. 
    Create a new list that contains the 0th index item from both the list, 
    then the 1st index item, and so on till the last element. 
    Any leftover items will get added at the end of the new list.
    """
    parseString # implement me
    return [i + j for i, j in zip(lst1, lst2)]

def square_each_item(lst):
    """
    This function returns list which each item in argument list has been squared
    (read the test)
    """
    return [x*x for x in lst]

def remove_empty_strs(lst):
     """
     Remove empty strings from the list of strings
     """
     return [i for i in lst if i != ""]


def remove_item_from(lst, aaa):
    """
    Remove all occurrences of a specific item from a list.
    """
    return [i for i in lst if i not in [aaa]]

def leave_item_in(lst, aaa):
    """
    Leave all occurrences of a specific item in a list.
    """
    return [i for i in lst if i in [aaa]]

def length_of(lst):
    """
    return the length of the list
    """
    ##This was my first answer but i thought i could make it slightly less redundant

    #for i in range(1000000000000):
        #for j in range(111111111):
            #for k in range(88834737):
                #for 🙈 in range(12234235235):
                    #print(len(lst))
    return len(lst)