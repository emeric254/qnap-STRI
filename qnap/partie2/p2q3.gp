
set terminal latex
set output "p2.q3.tex"
plot "p2.q3.data" u 1:2 t "minT", "p2.q3.data" u 1:3 t "maxT", "p2.q3.data" u 1:4 w l t "moyenne temps traitement", "p2.q3.data" u 1:5 t "minA" axes x1y2, "p2.q3.data" u 1:6 t "maxA" axes x1y2, "p2.q3.data" u 1:7 w l t "mayyenne nb packet att" axes x1y2
