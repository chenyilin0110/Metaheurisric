reset
set encoding utf8
set title "HC-SA-convergence"
set xlabel "Iteration"
set xrange [-10: 5000]
set ylabel "Distance"
set yrange [500: 1700]
plot "result/Avg/HC.txt" using 1:2 with lines title "HC",\
"result/Avg/SA.txt" using 1:2 with lines title "SA"

set terminal png
set output "result/Avg/HC-SA.png"
replot
set output
