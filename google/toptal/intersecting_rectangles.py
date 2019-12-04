import sys


# Determine if two rectangles intersect.
#
# 1. Solution when rects are defined by width, height and (x,y) coords of top-left corner
# 2. Solution when rects are defined by width, height and (x,y) coords of their centers
#
# What are behavior of edge cases?

# rect = (width, height, x, y)
def is_intersect(rect1, rect2):
    w1, h1, x1, y1 = rect1
    w2, h2, x2, y2 = rect2
    print(f'rect1  w:{w1} h:{h1} ({x1},{y1})     rect2  w:{w2} h:{h2} ({x2},{y2})')
    #print(f'rect1  ({x1},{y1})-({x1+w1-1},{y1+h1-1})')
    #print(f'rect2  ({x2},{y2})-({x2+w2-1},{y2+h2-1})')
    if x2 > x1 + w1 or x1 < x2 - w1 or y2 > y1 + h1 or y1 < y2 - h1:
        return False
    else:
        return True
    return rv


if __name__ == "__main__":

    rect1 = (10, 10, 5, 5)
    rect2 = (10, 10, 10, 10)
    rect3 = (20, 10, 40, 40)
    rect4 = (20, 20, 30, 30)
    print(is_intersect(rect1, rect2))
    print(is_intersect(rect1, rect3))
    print(is_intersect(rect2, rect3))
    print(is_intersect(rect3, rect4))


