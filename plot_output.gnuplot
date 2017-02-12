unset border
unset xlabel
unset ylabel
unset xtics
unset ytics
set term png
set output 'symbol.png'
set size square
p 'symbol.out' u 1:2 w l lw 4 lt 9 ti ''
