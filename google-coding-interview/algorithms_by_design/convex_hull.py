import sys
import math

# https://en.wikipedia.org/wiki/Quickhull
# https://codegolf.stackexchange.com/questions/11035/find-the-convex-hull-of-a-set-of-2d-points
# https://stackoverflow.com/questions/849211/shortest-distance-between-a-point-and-a-line-segment

# When you hammer a set of nails into a wooden board and wrap a rubber band around them,
# you get a Convex Hull.  Goal: Find the Convex Hull of a given set of 2D points.

"""
Input = a set S of n points
Assume that there are at least 2 points in the input set S of points
Quickhull (S)
(
    // Find convex hull from the set S of n points
    Convex Hull := ()
    Find left and right most points, say A & B, and add A & B to convex hull
    Segment AB divides the remaining (n-2) points into 2 groups S1 and S2
        where S1 are points in S that are on the right side of the oriented line from A to B,
        and S2 are points in S that are on the right side of the oriented line from B to A
    FindHull (S1, A, B)
    FindHull (S2, B, A)
    Output = Convex Hull
)

Use the sign of the determinant of vectors (AB,AM), where M(X,Y)
is the query point:

    position = sign((Bx - Ax) * (Y - Ay) - (By - Ay) * (X - Ax))

It is 0 on the line, and +1 on one side, -1 on the other side.


FindHull (Sk, P, Q)
(
    // Find points on convex hull from the set Sk of points
    // that are on the right side of the oriented line from P to Q
    If Sk has no point, then return.
    From the given set of points in Sk, find farthest point, say C, from segment PQ
    Add point C to convex hull at the location between P and Q
    Three points P, Q, and C partition the remaining points of Sk into 3 subsets: S0, S1, and S2
        where S0 are points inside triangle PCQ, S1 are points on the right side of the oriented
        line from P to C, and S2 are points on the right side of the oriented line from C to Q.
    FindHull(S1, P, C)
    FindHull(S2, C, Q)
)
"""

"""
public bool isLeft(Point a, Point b, Point c)(
     return ((b.X - a.X)*(c.Y - a.Y) - (b.Y - a.Y)*(c.X - a.X)) > 0;
)
Where a = line point 1; b = line point 2; c = point to check against.
If the formula is equal to 0, the points are colinear.
If the line is horizontal, then this returns true if the point is above the line.
"""

# a = line point 1; b = line point 2; c = point to check
# If the formula is equal to 0, the points are colinear.
# If the line is horizontal, then this returns true if the point is above the line.
# (The formula evaluates to 0 on the line, and +1 on one side, -1 on the other side.)
def is_left(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])) > 0

def is_right(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])) < 0


def sqr(x):
    return x * x

def dist2(v, w):
    return sqr(v[0] - w[0]) + sqr(v[1] - w[1])

def distToSegmentSquared(p, v, w):
  l2 = dist2(v, w)
  if l2 == 0: return dist2(p, v)
  t = ((p[0] - v[0]) * (w[0] - v[0]) + (p[1] - v[1]) * (w[1] - v[1])) / l2
  t = max(0, min(1, t))
  return dist2( p, (v[0] + t * (w[0] - v[0]), v[1] + t * (w[1] - v[1])) )

# distance from point p to line segment vw
def distToSegment(p, v, w):
    return math.sqrt(distToSegmentSquared(p, v, w))


convex_hull = {}

# Input = a set S of n points
# Assume that there are at least 2 points in the input set S of points
def Quickhull(S):
    # Find convex hull from the set S of n points
    global convex_hull
    convex_hull = {}
    # Find left and right most points, say A & B, and add A & B to convex hull
    A = B = None
    for (x,y) in S:
        if not A or x < A[0]:
            A = (x,y)
        if not B or x > B[0]:
            B = (x,y)
    convex_hull[A] = True
    convex_hull[B] = True
    # Segment AB divides the remaining (n-2) points into 2 groups S1 and S2
    #     where S1 are points in S that are on the right side of the oriented line from A to B,
    #     and S2 are points in S that are on the right side of the oriented line from B to A
    #for (x,y) in S:
    FindHull(S, A, B)   #(S1, A, B)
    FindHull(S, B, A)   #(S2, B, A)
    return [k for k in convex_hull]

def FindHull(Sk_all, P, Q):
    # Find points on convex hull from the set Sk of points
    # that are on the right side of the oriented line from P to Q
    Sk = [pt for pt in Sk_all if is_right(P, Q, pt)]

    if len(Sk) == 0: return     # if Sk contains no points, then return
    # From the given set of points in Sk, find farthest point, say C, from segment PQ
    farthest = (0, (None, None))
    for c in Sk:
        if distToSegment(c, P, Q) > farthest[0]:
            farthest = (distToSegment(c, P, Q), c)

    # Add point C to convex hull at the location between P and Q
    convex_hull[c] = True
    #print('added:', c)

    # Three points P, Q, and C partition the remaining points of Sk into 3 subsets: S0, S1, and S2
    #   where S0 are points inside triangle PCQ, S1 are points on the right side of the oriented
    #   line from P to C, and S2 are points on the right side of the oriented line from C to Q.
    FindHull(Sk, P, c)   #(S1, P, C)
    FindHull(Sk, c, Q)   #(S2, C, Q)


from math import *
# Uses a gift wrapping algorithm. The result starts with the leftmost point and wraps counter-clockwise.
#s=lambda(a,b),(c,d):atan2(d-b,c-a)
s=lambda t1,t2:atan2(t2[1]-t1[1],t2[0]-t1[0])
def h(l):
 r,t,p=[],pi/2,min(l)
 while 1:
    q=min(set(l)-{p},key=lambda q:(s(p,q)-t)%(2*pi));m=s(p,q);r+=[p]*(m!=t);p=q;t=m
    if p in r:return r


"""import operator
from functools import reduce
def test_lambda():
    li = [4, 3, 2, 1]
    rv = map(lambda x: x*x, li)
    print([x for x in rv])
    rv = reduce(lambda x,y:x*y, li)
    print(rv)
    add_one = lambda x: x + 1
    print(add_one(30))
    sys.exit()
    #if len(input_set & reduce(operator.__or__, user_set)) == 0:"""

"""def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

def square_numbers_gen(nums):
    for i in nums:
        yield (i*i)

#import mem_profile

def test_generator():
    my_nums = square_numbers([1,2,3,4,5])
    print(my_nums)
    my_nums = square_numbers_gen([1,2,3,4,5])
    print(next(my_nums))    
    print(next(my_nums))    
    print(next(my_nums))
    my_nums = square_numbers_gen([1,2,3,4,5])
    for num in my_nums:
        print(num, end=' ')
    print()
    my_nums = [x*x for x in [1,2,3,4,5]]    # list comprehension
    print(my_nums)
    my_nums = (x*x for x in [1,2,3,4,5])    # generator
    print(next(my_nums), next(my_nums))
    #print('Memory : {}Mb'.format(mem_profile.meory_usage_resource()))"""

if __name__ == "__main__":

    #test_generator()

    points = [(1, 1), (2, 2), (3, 3), (1, 3)]
    results = [(3, 3), (1, 3), (1, 1)]
    print(Quickhull(points))
    print(len(h(points)), len(results))

    points = [(4.4, 14), (6.7, 15.25), (6.9, 12.8), (2.1, 11.1), (9.5, 14.9), (13.2, 11.9), (10.3, 12.3), (6.8, 9.5),
        (3.3, 7.7), (0.6, 5.1), (5.3, 2.4), (8.45, 4.7), (11.5, 9.6), (13.8, 7.3), (12.9, 3.1), (11, 1.1)]
    results = [(13.8, 7.3), (13.2, 11.9), (9.5, 14.9), (6.7, 15.25), (4.4, 14),
        (2.1, 11.1), (0.6, 5.1), (5.3, 2.4), (11, 1.1), (12.9, 3.1)]
    print(Quickhull(points))
    print(len(h(points)), len(results))
    print(h(points) == results)

    points = [(1, 0), (1, 1), (1, -1), (0.68957, 0.283647), (0.909487, 0.644276), 
        (0.0361877, 0.803816), (0.583004, 0.91555), (-0.748169, 0.210483), 
        (-0.553528, -0.967036), (0.316709, -0.153861), (-0.79267, 0.585945),
        (-0.700164, -0.750994), (0.452273, -0.604434), (-0.79134, -0.249902), 
        (-0.594918, -0.397574), (-0.547371, -0.434041), (0.958132, -0.499614), 
        (0.039941, 0.0990732), (-0.891471, -0.464943), (0.513187, -0.457062), 
        (-0.930053, 0.60341), (0.656995, 0.854205)]
    results = [(1, -1), (1, 1), (0.583004, 0.91555), (0.0361877, 0.803816), 
        (-0.930053, 0.60341), (-0.891471, -0.464943), (-0.700164, -0.750994), 
        (-0.553528, -0.967036)]
    print(Quickhull(points))

    print(h([(1, 1), (2, 2), (3, 3), (1, 3)]))
    print(len(h(points)), len(results))

    

    


