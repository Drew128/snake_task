import numpy as np


n = int(input("n = "))
array = [[None for _ in range(n)] for _ in range(n)]                        # make an empty array

cur = {"x": 0, "y": 0, "dir": "r"}                                          # current position
directions = {"r": {"axe": "x", "step": 1}, "d": {"axe": "y", "step": 1}, "l": {"axe": "x", "step": -1},
              "u": {"axe": "y", "step": -1}}                                # definition of directions
rdlu = list(directions)                                                     # directions list


def turn():                                                                 # make a 90 degree turn right
    cur["dir"] = rdlu[(rdlu.index(cur["dir"])+1)%4]


def get_elem(pos):                                                          # get element from position
    return array[pos["y"]][pos["x"]]


def set_elem(pos, elem):                                                    # set element on position
    array[pos["y"]][pos["x"]] = elem


def step():                                                                 # make a 1 step in predefine direction
    where = directions[cur["dir"]]
    new = cur.copy()
    new[where["axe"]] += where["step"]
    return where, new                                                       # return direction and new position


def can_move(where, new):                                                   # is new position fits range
    if 0 <= new[where["axe"]] < n and not get_elem(new):                                    # and not filled yet
        return True


i = 1                                                                        # start from index = 1
while i < n**2:
    where, new = step()                                                      # try to make a step
    if can_move(where, new):                                                 # if step could be done
        set_elem(cur, i)                                                     # fill element on old position
        i += 1                                                               # increase the index
        cur = new                                                            # make a step
    else:
        turn()                                                               # make a turn if can`t move
        where, new = step()                                                  # and try to make a step
set_elem(cur, i)                                                             # fill the last position


print(np.array(array))                                                       # draw array

