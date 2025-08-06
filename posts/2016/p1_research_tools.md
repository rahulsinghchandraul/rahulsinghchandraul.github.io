## <center>A Need-to-Know for Researchers</center>

As researchers, we try to understand nature using scientific methods 
and come up with new interpretations. Our interpretations become 
meaningless unless we make it available to the rest of the world. An 
important question here is in what manner we convey our 
interpretations. In general, the process is done through scientific 
publications. That is, our idea is written into a document (either 
in paper or in electronic form). For the same, significant effort is 
required to filter out the required contents (text, analysis, 
figures, tables, and references) that need to be included in the 
document and to organize them in a meaningful way. In this article, 
I discuss six efficient free and open source software (FOSS) tools 
which provide the environment to make our work ready for publishing.

### 1. GNU/Linux

The use of computing systems and the availability of different
document creation tools help us to write our documents with minimum
effort. GNU/Linux is an operating system (OS) for our computer
machines which is freely (not in terms of cost) available. Unlike
Microsoft Windows and Apple's Mac OS, GNU/Linux is developed with the
philosophy of <a href="https://www.gnu.org/philosophy/free-sw.en.html"
target="_blank">Free Software</a>, i.e., knowledge is the wealth of
entire society, not a private property (For more information about
Free Software, read <a href="http://www.fsf.org" target="_blank">Free
Software Foundation</a>, <a href="https://stallman.org/biographies.html"
target="_blank">Richard Stallman</a>,
and <a href="https://www.gnu.org/licenses/gpl-3.0.en.html"
target="_blank">GNU General Public License</a>).

<table hspace="20" style="float:left" >
<tr><td><img src="figures/p1_linux_distros.png" height="200" width="400"></td></tr>
<tr><td align="center">Fig. 1: Linux
flavours <sup><a href="http://tecdistro.com/top-10-linux-distributions/"
target="_blank">&#x2608;</a></sup></td></tr>
</table>
	  
GNU/Linux offers several benefits such as user friendliness, free
of viruses, stability, security, free updates, and the rights provided
as a free software. At present, Linux distributions with different
flavours are available which can be downloaded from internet at no
cost. Examples include Ubuntu, Fedora, Debian, Arch, etc. Different
flavours of Linux distributions and their updated versions are
available at <a href="http://distrowatch.com" target="_blank">www.distrowatch.com</a>.

<a href="http://www.ubuntu.com" target="_blank">Ubuntu</a>
and <a href="https://getfedora.org" target="_blank">Fedora</a> are
popular due to its wide acceptance and support forums. The Linux
distributions are available as Live CDs such that you can try them
using a CD or a USB storage, i.e., without actually installing the
OS. User friendly graphical user interface allows the user to install
them to the machine (alone or along with other operating
systems). Since research requires a platform with stable software (for
nearly 4-5 years), Linux will be the best option in terms of
technology as well as philosophy. You can find installation steps for
several Linux distributions in the following links:
(a) <a href="http://www.ubuntu.com/download/desktop/install-ubuntu-desktop"
target="_blank">Ubuntu</a> and
(b) <a href="http://www.wikihow.com/Install-Fedora" target="_blank">Fedora</a>.

### 2. GNU Typist
	  
Since we all are computer users, we cannot avoid typing. However,
we may not be aware of how much time we are unnecessarily spending due
to the inefficient movement of our fingers and hands on the
keyboard. Significant amount of time can be saved if we avoid the hand
movements and concentrate only on the finger movements to type the
letters. An easy way to achieve the same is to learn typing. Several
software as well as online tools are available to self-learn
typing. For the sake of this article, I suggest a
tool <a href="https://www.gnu.org/software/gtypist/index.html"
target="_blank">GNU Typist</a>, a free software, to learn typing. GNU
Typist is a command line typing tutor which can be easily installed
from the software center in Linux or using the following command in
terminal.

$ <font color="#003380">sudo apt-get install gtypist</font>

In order to run GNU Typist, run the command in the terminal as
follows:

$ <font color="#003380">gtypist</font> 

You can see the instructions for continuing with the course. The
course is divided into basic lessons of typing with a set of letters
per each lesson. Also, upon completion of each exercise, you will get
your performance in terms of different metrics, so that you can repeat
the exercise to achieve the required performance.
	  
It requires lot of patience at the initial stages of learning (Only
for first 3-4 days). You may feel a little bit of pain in your fingers
or lack of interest, which may force you to go back to your previous
typing style, which is strictly not recommended. After 4-5 days,
the <em>lack</em> of interest will turn to <em>more</em> interest and
the urge to type will increase as days go on. At the end, you can
measure your typing speed using the metrics such as words per minute
(WPM) and typing accuracy. It will be sufficient that if you can
achieve 60 WPM or above.

### 3. GNU Emacs
	  
<img src="figures/p1_emacs_icon.png" height="100" width="100" hspace="20" style="float:left"><a href="https://www.gnu.org/software/emacs/"
target="_blank">GNU Emacs</a> is a free editor using which we can do,
whatever we want to do with a computer. You may not believe my first
statement. It is better to experience it. In simple words, the Emacs
text editor can be controlled using keyboard alone, with short-cuts,
especially the <em>Ctrl</em> and <em>Alt</em> keys. We can move to any
position of your document without using the dedicated direction keys
such as arrow keys, Home, PgUp, PgDn and End. We do not need to change
the hand-position that we learned from GNU Typist. That is, only the
finger movements are sufficient to control the entire environment.

Apart from a simple editor, Emacs provides support to the specific
environment that we are working with. For example, it
provides <em>python-mode</em> for Python programmers to make the
coding easier with features such as auto-completion and
auto-indentation. For LaTeX users, Emacs provides AUCTeX with
shortcuts for LaTeX environment. Even, we can customize
the environment for our requirements. In order to install Emacs, run
the following command in the terminal.
	    
$ <font color="#003380">sudo apt-get install emacs24</font>
	  
Emacs can be run either with a graphical user interface (GUI) or in
terminal. You can use the following commands to run Emacs. For
GUI mode<br>

$ <font color="#003380">emacs</font> 

For terminal mode

$ <font color="#003380">emacs -nw</font>

Similar to GNU Typist, upon opening Emacs, you can see the
instruction set to start with. By pressing <em>Ctrl-h t</em>, you will
be redirected to an Emacs tutorial where you can read and practice at
the same place. Be cautious that you will be irritated with the
shortcuts at the beginning, similar to the beginning stage of
typing. Spend a few days with Emacs by ignoring such distractions. One
important point to note, regarding both typing as well as Emacs, is
that your fingers will learn these two tools rather than your
conscious mind. After learning, you may not able to answer where the
position of a particular key in the keyboard is or what is the
shortcut for a particular activity in Emacs. However, your fingers
will do it perfectly without the involvement of your conscious
mind. Here, reality comes as the biggest joke.

### 4. LaTeX
	  
<img src="figures/p1_latex_bird.png" height="104" width="130"
hspace="20" style="float:left"><a href="https://www.latex-project.org/"
target="_blank">LaTeX</a> is an extreme-quality document creation tool
originally developed by <a href="http://www.lamport.org"
target="_blank"> Leslie Lamport</a>. LaTeX makes use of
the <a href="http://tug.org/" target="_blank">TeX</a> type setting
system primarily developed by <a href="http://cs.stanford.edu/~uno/"
target="blank">Donald E. Knuth</a>. The word <em>Documents</em>
includes reports, figures, and presentation slides. While creating
documents in conventional tools such as Microsoft Office, OpenOffice,
or LibreOffice, you can feel that major part of your time is consumed
on the alignment, orientation, or the placement of document content
instead of the content, which is the important part. LaTeX solves this
problem by automating the style related issues and makes the user to
concentrate only on the content. We need to write the content with
respective command or environment to make this work. However, the
learning time of basic commands, even though you may find it difficult
at the initial stage, is not at all comparable with the quality that
you get from the documents. A tutorial for beginners from the TeX
Users Group (TUG) can be downloaded
from <a href="https://www.tug.org/twg/mactex/tutorials/ltxprimer-1.0.pdf"
target="_blank">here</a>. As mentioned in the previous section, Emacs
provides the LaTeX environment to edit documents using AUCTeX
package. (For a very simple tutorial visit: <a href="../2010/p1_latexexperience.html" target="_blank">An
Experience with LaTeX</a>).

Apart from articles, letters, reports, books, or scientific papers,
LaTeX is used to create presentation slides with the help of a class
called <em>Beamer</em>. The slides are created using
the <em>frame</em> environment. The beamer class is originally developed
by <a href="http://www.tcs.uni-luebeck.de/en/mitarbeiter/tantau/"
target="_blank">Till Tantau</a> and currently maintained
by <a href="https://github.com/josephwright" target="_blank">Joseph Wright</a> and <a href="https://vedran.miletic.net/"
target="_blank">Vedran Mileti&#263;</a>. Beamer themes are usually
named using place names (such as Copenhagen, Berkeley, Frankfurt, and Warsaw) and you can define your own theme if required
(See <a href="https://www.hartwork.org/beamer-theme-matrix/"
target="_blank">beamer theme matrix</a>). A user guide for beamer can
be downloaded
from <a href="http://texdoc.net/texmf-dist/doc/latex/beamer/doc/beameruserguide.pdf"
target="_blank">here</a>.

In addition to technical papers and presentation slides, posters
are important method to convey our ideas and results. LaTeX allows us
to create high quality posters with appropriate dimension. If we are
comfortable TikZ drawing, we can create custom posters of required
size. Free LaTeX templates for posters are available at the following links:
(i)<a href="https://www.overleaf.com/gallery/tagged/poster#.WGVA1PF9600"
target="_blank">Link-1</a>,
(ii) <a href="http://www.latextemplates.com/cat/conference-posters"
target="_blank">Link-2</a>, and
(iii) <a href="http://www.brian-amberg.de/uni/poster/"
target="_blank">Link-3</a>.

One of the major addition to the TeX system is the graphics package
named <em>TikZ</em>. It includes macros for writing mathematical
descriptions of an image, using which the PDF can be produced with the
LaTeX engine. Major part of the TikZ library is developed
by <a href="http://www.tcs.uni-luebeck.de/en/mitarbeiter/tantau/"
target="_blank">Till Tantau</a> and the remaining development is done
by Christian Feuersaenger. Drawing in TikZ becomes easier if we have
the cartesian coordinate system in mind while writing the image
description. It may take a few days, similar to typing or Emacs, to
get familiarized with the drawing commands. However, the quality of
the figure is incomparable with the images produced using other
tools. You can see the magic of TikZ
in <a href="http://www.texample.net/tikz/examples/all/"
target="_blank">www.texample.net</a>. Nowadays, the drawing tools
generate the TeX code corresponding to our figure allow us to save the
drawings as a <em>.tex</em> file (instead of image formats such
as <em>.png, .jpg</em>, or <em>.eps</em>), so that we can create the
figure using LaTeX.  An introduction for drawing using TikZ is
available <a href="http://cremeronline.com/LaTeX/minimaltikz.pdf"
target="_blank">here</a>.

### 5. Python
	  
<img src="figures/p1_python_icon.png" height="104" hspace="20"
style="float:left"><a href="https://www.python.org/" target="_blank">Python</a> is
an open source interpreted programming language which provides a
platform to express our ideas in mind with minimum effort. As
<a href="http://homepages.cwi.nl/~jack/" target="_blank">Jack Jenson</a>  says,
<em>&ldquo;Python is a truly wonderful language. When somebody comes
up with a good idea it takes about 1 minute and five lines to program
something that almost does what you want. Then it takes only an hour
to extend the script to 300 lines, after which it still does almost
what you want.&rdquo;</em> Python was developed by a Dutch
programmer, <a href="https://gvanrossum.github.io//" target="_blank">Guido van
Rossum</a>.  We can learn the language within hours (this phrase is
not an exaggeration), and start writing our codes easily. Since Python
is easy to learn, it became the top introductory programming language
at the U.S. universities <sup><a href="http://cacm.acm.org/magazines/2015/3/183588-python-for-beginners/fulltext"
target="_blank">&#x2608;</a></sup>. From my perspective, if you have written 1+2 for adding
the numbers 1 and 2 (either in paper or in calculator), you are
already a Python programmer, because 1+2 is the python code to add the
numbers 1 and 2. Unlike other popular languages such as C, C++, or
Java, Python is free from punctuation marks (such as
semi-colons and braces) and language constructs, which usually make students afraid of
learning language and, thereby, discouraging them to write
code. On the other hand, Python insists proper indentations (spaces at the
beginning) for code blocks to make the code more organized and
readable to keep up with the design philosophy of Python. Two of the most popular
versions Python are Python 2.7 and 3.0.
	  
Python supports variety of programming paradigms such as functional
programming, object oriented programming (popularly known as OOP),
aspect oriented programming, and structured programming. The wide
acceptance of Python resulted in the development of code libraries for
a variety of computing operations. Some of them
include <a href="http://www.scipy.org/" target="_blank">SciPy</a> (for science and
engineering), <a href="http://www.scipy.org/" target="_blank">NumPy</a> 
(numerical analysis), <a href="http://matplotlib.org/" 
target="_blank">matplotlib</a> (graph 
plotting), <a href="http://pyopengl.sourceforge.net/" target="_blank">PyOpenGL</a>
(high performance graphics), <a href="http://www.sympy.org/en/index.html" target="_blank">SymPy</a>
(symobolic mathematics), <a href="https://networkx.github.io/"
target="_blank">NetworkX</a>, <a href="http://igraph.org/python/" target="_blank">igraph</a>
(graph theory and network
analysis), <a href="http://pygame.org/hifi.html" target="_blank">pygame</a> (games and
art), <a href="http://scikit-learn.org/stable/"
target="_blank">scikit-learn</a>, <a href="http://mlpy.sourceforge.net/"
target="_blank">mlpy</a>
(machine learning), and <a href="http://pandas.pydata.org/" target="_blank">pandas</a>
(data analysis). You can write Python code in any basic text editor
and save as a <em>.py</em> file and execute using a command line
interpreter. In addition, there exist several dedicated development environments, which
include Integrated Development and Learning Environment
(<a href="https://docs.python.org/2/library/idle.html" target="_blank">IDLE</a>),
<a href="http://www.red-bean.com/doc/pymacs/html/pymacs.html" target="_blank">PyMacs</a>
(Emacs extension for Python), <a href="http://drpython.sourceforge.net/" target="_blank">DrPython</a>,
and <a href="https://ipython.org/" target="_blank">IPython</a>.
	  
Similar to libraries, Python is rich in terms of learning resources
as well. One of the best slides from Rossum is available
from <a href="http://people.csail.mit.edu/rudolph/Teaching/Lectures/guido-intro-1.pdf"
target="_blank">here</a>,
using which you can learn the language within a couple of hours. Other
useful materials include
(i) <a href="http://www.diveintopython.net/" target="_blank">Dive into Python</a>,
(ii) <a href="http://www.ibiblio.org/swaroopch/byteofpython/files/120/byteofpython_120.pdf"
target="_blank">A
Byte of Python</a>,
(iii) <a href="http://www.greenteapress.com/thinkpython/thinkCSpy.pdf"
target="_blank">How
to Think Like a Computer Scientist: Learning with Python</a>,
(iv) <a href="http://www.goodreads.com/book/show/80444.Python_Essential_Reference"
target="_blank">Python Essential Reference: Developer's Library</a> and (v)
<a 
href="http://www.goodreads.com/book/show/80444.Python_Essential_Reference" target="_blank">Learn
Python: Tutorials Point</a>.

<b><em>Note:</em></b> If you are comfortable with MATLAB, free and
open source software alternatives are available with similar syntax and features
as that of MATLAB. Two of the most important tools are
(i) <a href="http://www.scilab.org/">Scilab</a> and
(ii) <a href="https://www.gnu.org/software/octave/">GNU Octave</a>. 

### 6. Gnuplot

<img src="figures/p1_gnuplot_icon.png" height="48"
hspace="20"
style="float:left"><a href="http://www.gnuplot.info/" target="_blank">Gnuplot</a> is a
2D and 3D plotting tool for graphical visualization of data. It uses a
command line interpreter to execute the commands for plotting. Gnuplot
is easy to learn and is integrated with basic programming
constructs (such as loops and conditional statements) to manage
complex data patterns. It supports a variety of image formats such
as <em>jpeg, png, eps, svg, fig, gif, </em> and <em>LaTeX</em>. If you
are familiar with LaTeX, I recommend to use the LaTeX output such that
the figure can be created using TikZ with extreme quality (See my
post: <a href="../2015/p1_gnuplotlatex.html" target="_blank">Gnuplot + LaTeX: The
Ultimate Plotting Experience</a>).

It is easy to learn gnuplot from examples rather than from
textbooks. A detailed library of different types of plots are
available in <a href="http://gnuplot.sourceforge.net/demo/" target="_blank">gnuplot
demos</a>. Some of the materials to learn gnuplot include
(i) <a href="http://gnuplot.sourceforge.net/docs_4.6/gnuplot.pdf" target="_blank">gnuplot
4.6: An Interactive Plotting Program</a>,
(ii) <a href="http://www-bs2.informatik.uni-tuebingen.de/services/nilse/books/GnuplotinAction.pdf"
target="_blank">
Gnuplot in Action: Understanding Data with Graphs</a>, and
(iii) <a href="http://gnuplot.sourceforge.net/docs_4.0/gpcard.pdf" target="_blank">
gnuplot Quick Reference</a>.

I consider the tools discussed above are highly efficient in terms
of time, effort, and quality. Even though it takes a little time to
learn the tools (only a matter of 1 or 2 weeks), the tools will surely
remain as an asset for the remaining of our life.

<br>
------------------------------------<br>
Thanks for <b>Deepak Gopalakrishnan</b> for suggestions. If you find 
any mistakes or you have any suggestions, please send me a mail.
