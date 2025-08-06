
### <center>Gnuplot + LaTeX:&nbsp; The Ultimate Plotting Experience</center>
	  
<img src="figures/p1_graph_icon.png" hspace="20" style="float:left">
Plotting graphs is an important activity for most of our analysis
work. Usually we have a function, say *y = f(x)* , and a sample of
*(x,y)* pairs. In order to analyze the behavior of the function, we
represent the *x* and its corresponding *y* values as a graph. We draw
a horizontal *x*-axis and a vertical *y*-axis. In the graph, we
represent each *(x,y)* pair as a dot or a cross in the *x-y*
plane. Instead of points, we can connect the points with lines or can
draw vertical bars (histograms) corresponding to each *y* value to get
more meaningful interpretation of the function. This post is intended
to provide information on generating extreme quality graphs using two
of the important tools, **Gnuplot** and **LaTeX**.

For the remaining of this post, I assume that you have a basic
knowledge of Gnuplot and LaTeX. For plotting using this method, we
need to have **TikZ** and **LuaTeX** libraries installed. Use the
following command (in GNU Debian/Ubuntu systems) if your system does
not have them.

$ <font color="#003380">sudo apt-get install gnuplot latexmk pgf
preview-latex* texlive-fonts-recommended luatex texlive-pictures
texlive-latex-extra</font>

Assume that we have a text file *data.txt* with input data (the
*(x,y)* pairs) for plotting. For example, you have the speed of a car
and a bus at certain time instants. A sample file is as follows.

- - - -
**Time Car Bus**  
1 10 35  
2 45 20  
3 30 40  
4 25 10  
5 60 55<br>

- - - -


As the next step, write the Gnuplot script for plotting the graph.
The following is a sample code, saved as *plot.gp*.  

----------------------------------------------------------------------------------------  
<span style="color:#808080;"># Enabling the terminal in LaTeX TikZ mode</span><br>
<span style="color:#000000;">set</span> <span style="color:#008000;">term</span>
<span style="color:#000000;">tikz standalone color solid</span><br>
<span style="color:#808080;"># Enabling the dashed line option</span><br>
<span style="color:#000000;">set</span> <span style="color:#008000;">termoption</span> <span style="color:#000000;">dash</span><br>
<span style="color:#808080;"># Setting output file  name</span> <span style="color:#808080;">(Here output is a LaTeX file)</span><br>
<span style="color:#000000;">set</span> <span style="color:#008000;"> output</span> <span style="color:#333399;">'figure.tex'</span><br>
<span style="color:#808080;"># Set title</span><br>
<span style="color:#000000;">set</span> <span style="color:#008000;">title</span>
<span style="color:#333399;">'Speed Vs Time'</span><br>
<span style="color:#808080;"># Set labels for x and y axes</span><br>
<span style="color:#000000;">set</span> <span style="color:#008000;">xlabel</span>
<span style="color:#333399;">'Time (in minutes)'</span><br>
<span style="color:#000000;">set</span> <span style="color:#008000;">ylabel</span> <span style="color:#333399;">'Speed (km/hr)'</span><br>
<span style="color:#808080;"># Set the legend</span><br>
<span style="color:#000000;">set</span> <span style="color:#008000;">key</span> <span style="color:#000000;">horiz top left Left box spacing 2 sample 2</span><br>
<span style="color:#808080;"># Plot the graph</span><br>
<span style="color:#000000;">plot</span> <span style="color:#ff9900;">'data.txt'</span>
<span style="color:#000000;">u</span> <span style="color:#333399;">1:2</span>
<span style="color:#000000;">w lp lt 1 pt 5 lc rgb 'dark-blue' t columnheader,\ <br>
<span style="color:#000000;">'data.txt' u 1:3 w lp lt 2 pt 7 lc rgb 'dark-green' t columnheader</span><br>

----------------------------------------------------------------------------------------


Execute the Gnuplot code <em>plot.gp</em> using the following command.

$ <font color="#003380">gnuplot plot.gp</font>

Execution creates a file *figure.tex* with the TikZ script for drawing
the graph. TikZ is used to draw high quality figures in LaTeX (See <a
href="http://www.texample.net" target="_blank">TeXample</a>). Thanks
to Gnuplot's support for TikZ terminal, which allows us to generate a
*tex* file, with scripts to draw the graph, instead of normal image
formats such as *jpeg* or *png*. As the final step, we need to compile
the file *figure.tex* with *pdflatex*.

$ <font color="#003380">pdflatex figure.tex</font>

A file <a href="figures/p1_figure.pdf"
target="_blank">*figure.pdf*</a> will be generated with the
graph. There hardly exist tools to create graphs of higher quality
similar to Gnuplot + LaTeX. Since the graph is created using LaTeX,
the default font will be the same as the default font provided by
LaTeX. Also, LaTeX allows to import figures with *.pdf* extension
using *\includegraphics{}* command. Presence of such figures improves
the effective quality of technical papers.

<br>-----------------------<br>
Send me suggestions or corrections if any.
