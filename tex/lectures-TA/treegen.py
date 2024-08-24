

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
    radius=0.1mm
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
    for i in range(1,n+1):
        l = int(log2(i)) 
        u = 2 **(l+1)
        j = i - 2**int(log2(i))
        if l > 3:
            q = 2 
        else:
            q = 1 
        texcode+=f"\\node [every  neuron ] (v-{i}) at ( { q*  k*(j)/u } ,-{int(log2(i))}) {{ ${arr[i-1]}$  }};"
    
    for i in range(1,n+1):
        if 2*i < n+1 :
            texcode+=f"\\draw [->] (v-{i}) -- (v-{2*i});"
        if 2*i +1  < n+1 :
            texcode+=f"\\draw [->] (v-{i}) -- (v-{2*i+1});"
    
    texcode += r"""\end{tikzpicture}"""
                #\end{adjustbox}"""

#\begin{adjustbox}{width=\textwidth}
    _file.write(texcode)


def runnig_example():
    gen_heap([1,4,2,5,6,2,3], "tree-41") 
    gen_heap([3 ,4,2,5,6,2], "tree-42") 
    gen_heap([2,4,3,5,6,2], "tree-43") 
    gen_heap([2,4,2,5,6,3], "tree-44")
from heapq import heapify
from random import randint 
def random_heap( a, b , K, name , sign = 1):
    L = [ randint(a,b) for _ in range(K) ] 
    L = [ (v * sign , u)  for (v,u) in zip(L,L)]
    heapify(L)
    gen_heap( [ u for (v,u) in L ] , name) 

def main():
    runnig_example()
    random_heap( 150, 342, 17, "tree-r1") 
    random_heap( 5, 150, 17, "tree-r2", sign = -1)
    #gen_heap([1,4,2,5,6,3], "tree-4") 
    #gen_heap([11,41,22,55,65,31,81,82,83,84,85,86,87,88,89], "tree-5" )
    #gen_heap([9,8,7,6,5,4,3,2,1,0.5,0.4,0.3,0.2,0.1], "tree-6" )
if __name__ == "__main__":
    main()
