#for a given list, create a function that prints out series of stars corresponding to list length.


def draw_star(li):
    star = "*"
    for i in li:
        if isinstance(i, int):
            print "*" * i
    
        elif isinstance(i, str):
            length = len(i)
            letter = i[0].lower()
            print letter*length

x = [4, 6, 1, "kingdom", 5, 7, 25]

draw_star(x)


#part 2