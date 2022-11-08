

from math import log2


def main():
    _file = open("tree.tex", "w")
    texcode = r"""
    % Drawing a graph using the PG 3.0 graphdrawing library
% Author: Mark Wibrow
%\documentclass[tikz,border=10pt]{article}
%\usepackage{tikz}
%\usetikzlibrary{positioning}
%\begin{document}

\tikzset{%
  every neuron/.style={
    circle,
    draw,
    %fill=black,
    radius=0.05mm
  },
  neuron missing/.style={
    draw=none,
    scale=2,
    text height=0.25cm,
    execute at begin node=\color{black}$\vdots$
  },
}
\begin{adjustbox}{width=\textwidth}
\begin{tikzpicture}
    """
    n = 16 
    for i in range(1,n):
        j = i - 2**int(log2(i))
        texcode+=f"\\node [every  neuron ] (v-{i}) at ( {j} ,-{int(log2(i))}) {{ ${i}$  }};"
    
    for i in range(1,int(n/2)):
        texcode+=f"\\draw [->] (v-{i}) -- (v-{2*i});"
        texcode+=f"\\draw [->] (v-{i}) -- (v-{2*i+1});"
    
    texcode += r"""\end{tikzpicture}
                \end{adjustbox}"""


    _file.write(texcode)

if __name__ == "__main__":
    main()
