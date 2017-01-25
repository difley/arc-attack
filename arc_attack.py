#!/usr/bin/env python

import scipy
import sys


def aa():
    state = {'x_center': 0.,
             'y_center': 0.,
             'direction': 1,
             'start_angle': 0.,
             'end_angle': 9.*scipy.pi/5.,
             'radius': scipy.random.random()}
    cx = 0.
    cy = 0.
    direction = 1
    thetai = 0.
    r = scipy.random.random()
    thetaf = thetai + 9.*scipy.pi/5.
    dist = 1.
    for j in range(1000):
        arc(cx,
            cy,
            r,
            direction,
            thetai,
            thetaf)
        state['x_center'], state['y_center'] = line(cx,
                     cy,
                     r,
                     direction,
                     thetaf,
                     dist)
        dist = nextline()
        cx, cy, r, direction, thetai, thetaf = nextarc(cx,
                                                       cy,
                                                       r,
                                                       direction,
                                                       thetai,
                                                       thetaf)


def nextarc(cx, cy, r, direction, thetai, thetaf):
        #sign randomly is 1 or -1.  if sign==1,
        #next circle's center is on convex side of
        #current circle, else next center is
        #on concave side of current circle
        sign = scipy.random.randint(2)*2 - 1
        #sign = 1
        direction = -direction*sign
        #new thetai is on opposite side of circle from thetaf
        if (sign == 1):
            thetai = thetaf + scipy.pi
        else:
            thetai = thetaf
        #put thetai in the range 0<thetai<2pi
        thetai = scipy.fmod(thetai, 2.*scipy.pi)
        if thetai < 0.:
            thetai += 2.*scipy.pi
        rold = r
        r = scipy.random.random()*0.2 + 0.2
        cx += (sign*r + rold)*scipy.cos(thetaf)
        cy += (sign*r + rold)*scipy.sin(thetaf)
        thetaf = thetai + scipy.random.random()*2.*scipy.pi
        return cx, cy, r, direction, thetai, thetaf


#return arc points specified by present state
#precondition: if direction != -1 (clockwise arc),
#then thetai < thetaf.
#pointdens is a positive real number.
#postcondition: direction==-1 for a clockwise arc,
#else anti-clockwise arc is produced.
def arc(cx, cy, r, direction, thetai, thetaf, pointdens=3):
    tf = thetaf
    if (direction == -1) and (thetai < thetaf):
        tf -= 2.*scipy.pi
    np = int(abs(tf - thetai)*pointdens)
    for i in range(np):
        ang = (tf - thetai)*float(i)/float(np) + thetai
        print("%f %f" % (r*scipy.cos(ang) + cx, r*scipy.sin(ang) + cy))

def nextline():
    return scipy.random.random()*1.0 + 0.3

#precondition: dist>0
def line(cx, cy, r, direction, thetaf, dist, pointdens=4):
    np = int(dist*pointdens)
    x0 = r*scipy.cos(thetaf) + cx
    y0 = r*scipy.sin(thetaf) + cy
    for i in range(np):
        print("%f %f" % (x0 -
        direction*dist*float(i)/float(np)*scipy.sin(thetaf), y0 +
        direction*dist*float(i)/float(np)*scipy.cos(thetaf)))
    return cx - direction*dist*scipy.sin(thetaf), cy + direction*dist*scipy.cos(thetaf)

def main():
    scipy.random.seed(int(sys.argv[1]));
    aa()


if __name__ == '__main__':
    main()
