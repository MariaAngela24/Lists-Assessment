"""List Assessment 

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """

    only_odd_numbers = []
    for item in numbers:
        if item % 2 != 0:
        #This command checks if number as odd by checking if remainder is 0
        #when number is divided by 2
            only_odd_numbers.append(item)
    return only_odd_numbers


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo
    """

    for item in items:
        print items.index(item), item


def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale"],
        ...     ["hummus", "beets", "bagel", "lentils", "kale"]
        ... )
        ['bagel', 'kale']

    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """

    return ['the wrong thing']

    #For every item in first list 
    #if index of item in second list is not None
    #add the item to a set 
    #Turn set back into a sorted list

    #I skipped this and meant to come back to it but did not realize until I 
    #was checking my work that I never finished it.  My initial thought about
    #how to solve it would be to start by using a function to compare each item 
    #in one list to the items in the other list and the delete the items that do 
    #not appear in both lists.  The same thing would then need to be done with the
    #second list so only the items in common remain.  One of the two lists could then
    #be turned into a set, which will eliminate all duplicates.  Set could then be turned
    #back into a list and sorted.  Even though I think that would work if I could figure
    #out all the commands, it does not seem efficient....


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """
    every_other = items[0::2]
    #This command captures the first item in the list and then captures every
    #other item in the rest of the list
    return every_other


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """
    sorted_items = sorted(items)
    if n == 0:
        largest_items = []
    #In command below, Python reads 0 as first item in list. 
    #Above command ensures program returns empty set if n==0
    else:
        largest_items = sorted_items[-n::]
    #Sorting input and copying n largest integers to new list
    return largest_items

    


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
