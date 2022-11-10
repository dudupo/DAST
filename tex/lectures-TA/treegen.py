

from math import log2


def gen_heap(arr, _name):
    _file = open(f"{_name}.tex", "w")
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

\begin{tikzpicture}
    """
    n = len(arr) 
    k = (n // 2)*2
    for i in range(1,n):
        l = int(log2(i)) 
        u = 2 **(l+1)
        j = i - 2**int(log2(i))
        texcode+=f"\\node [every  neuron ] (v-{i}) at ( {k*(j)/u } ,-{int(log2(i))}) {{ ${arr[i-1]}$  }};"
    
    for i in range(1,int(n/2)):
        texcode+=f"\\draw [->] (v-{i}) -- (v-{2*i});"
        texcode+=f"\\draw [->] (v-{i}) -- (v-{2*i+1});"
    
    texcode += r"""\end{tikzpicture}"""
                #\end{adjustbox}"""

#\begin{adjustbox}{width=\textwidth}
    _file.write(texcode)


def main():
    gen_heap([11,41,22,55,65,31,81,82,83,84,85,86,87,88,89], "tree-5" )
    gen_heap([9,8,7,6,5,4,3,2,1,0.5,0.4,0.3,0.2,0.1], "tree-6" )
if __name__ == "__main__":
    main()
