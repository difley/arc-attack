#!/bin/bash
set -u
set -e
prefix=$1
gnuplot << HERE
    unset border
    unset xlabel
    unset ylabel
    unset xtics
    unset ytics
    set term png
    set output '${prefix}.png'
    set size square
    p '${prefix}.out' u 1:2 w l lw 4 lt 9 ti ''
HERE
open -a /Applications/Preview.app "${prefix}.png"
