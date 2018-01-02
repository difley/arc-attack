
-----------------------
Arc Attack
-----------------------
A pseudorandom, procedural art generator. Arcs and line segments team up to generate a continuous curve.


-----------------------
Motivation for doing this
-----------------------
I'm fascinated by procedural art and computational geometry. I wrote this program to explore how circular arcs and line segments can be joined together to generate visually pleasing curve.
![Random curve overlapping example (rendered with Gnuplot)](images/random_curve_overlapping.png)
![Polygon example](images/polygon.png)
![Wavy polygon example](images/wavy_polygon.png)
![Spiral example](images/spiral.png)
![Random curve nonoverlapping example](images/random_curve_nonoverlapping.png)


-----------------------
Prerequistes
-----------------------
   python 3.3+ (run script requires python3's `venv` module)
   
   gnuplot (to visualize the output)

   MacOS Preview (to visualize the output)


-----------------------
How to run the examples
-----------------------
Five examples are provided in the examples/ folder. To run the wavy polygon example, use these commands in the shell:
    git clone https://github.org/difley/arc-attack.git
    cd arc_attack/examples/wavy_polygon
    bash run.sh


The other four examples can be run analogously by browsing to each of the corresponding example folders and running:
    bash run.sh 
