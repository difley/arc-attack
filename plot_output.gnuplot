unset border
unset xlabel
unset ylabel
unset xtics
unset ytics
set term png
set output 'output.png'
set size square
p 'output.out' u 1:2 w l lw 2 lt 9 ti ''
