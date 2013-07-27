from merge_sort_2d import *
import math, random, re

def pre(points):
    '''Pre-process for closest pair problem, 'points' being a list of 2-tuples.
    return two ordered list based on x and y coordinates using merge sort.'''

    px = merge_sort_2d(points, 0)
    py = merge_sort_2d(points, 1)
    return px, py

#print pre([(1,9),(45,6),(7,25),(89,9),(76,39),(63,86),(0,37)])

def dist(pair):
    '''Calculate the distance between a pair of two points (list)'''
    try:
        a, b = pair[0], pair[1]
        return math.sqrt((a[0] - b[0])**2 + (a[1] -b[1])**2)
    except:
        return None

def closest_split_pair(Px, Py, delta):
    '''return possible point pair whose distance is smaller than delta'''

    mid = int(len(Px)/2)
    x_bar = Px[mid-1][0] #biggest x-coordinate in left of P
    bar_pts = [p for p in Py if ((x_bar-delta) <= p[0] <= (x_bar+delta))]
    best = delta
    best_pair = None
    for i in range(0, len(bar_pts)):
        for j in range(0, min(7, len(bar_pts)-i)):
            if i == (i + j):#make sure not double count same point
                continue
            pair = [bar_pts[i], bar_pts[i+j]]
            if dist(pair) < best:
                best_pair = pair
                best = dist(pair)
    return best_pair

def closest_pair(Px, Py):
    '''Divide the points into 2 halves, left and right, for each sorted copies of
    the original data, find the closest pair in each half, compare with the possible
    closest pairs, of which each point in different halves, return the minimum.'''

    mid = int(len(Px)/2)
    left_x = Px[:mid]
    right_x = Px[mid:]
    left_y = Py[:mid]
    right_y = Py[mid:]
    pair_dist = []

    #base case
    if len(Px) == 1:
        return None
    elif len(Px) == 2:
        return Px
    else:
        left = closest_pair(left_x, left_y) #left is a list of two points
        right = closest_pair(right_x, right_y)
        #if None is in (left, right), it has to be left
        if left == None:
            delta = dist(right)
        else:
            delta = min(dist(left), dist(right))
        split = closest_split_pair(Px, Py, delta)
        pair_dist = [(x, dist(x)) for x in (left, right, split) if x]
        return merge_sort_2d(pair_dist, 1)[0][0]

def closestPair(points):
    '''Wrapper function'''

    Px, Py = pre(points)
    return closest_pair(Px, Py)

#test cases
pts1=[(1,2),(2,5),(6,4)]
print closestPair(pts1)
rand_pts = []
#random.seed(3)
for i in range(100):
    a, b = random.randint(0, 100), random.randint(0, 100)
    if (a,b) not in rand_pts:
        rand_pts.append((a,b))
print closestPair(rand_pts)
