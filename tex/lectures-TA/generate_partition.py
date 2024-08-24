

from math import log2
from random import randint


TIKZ = [ ]

def gen_raw(_arr, i , j):

    ret = r"""\vet{""" 
    for _, val in enumerate(_arr):
        if _ not in [i,j]:
            ret += str(val) 
        else:
            ret += r"""\re""" +  str(val) 
        ret += ", "
    return ret[:-2] + r"""} & \\ """

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]
    global TIKZ
    TIKZ += [gen_raw(A, i ,j)]
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            swap(A, i, j)
    if i+1 != r:
        swap(A, i+1 ,r)
    return i+1

def randomized_partition(A, p, r):
    i = randint(p,r)
    print(i)
    swap(A, i, r)
    return partition(A, p, r)

def quicksort(A, p, r):
    
    if p < r:
        global TIKZ
        TIKZ += [gen_raw(A, p, r).replace("\\re", "\\bl").replace("\\\\", f"quicksort$(A,{p},{r})$\\\\")]

        q = randomized_partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
    
def test_quciksort():
    global TIKZ 
    for A in [ [1, 2, 3, 4, 5, 6],
               [1, 3, 2, 4, 5, 6],
               [1 , 5, 1, 5,3, 2, 1]]:
        print(A)
        quicksort(A,0, len(A)-1)
        print(A)
        print(TIKZ)
        TIKZ = ""





def gen_run(arr, _name):
    _file = open(f"{_name}.tex", "w")
    texcode = r"""
    % Drawing a graph using the PG 3.0 graphdrawing library
% Author: Mark Wibrow
%\documentclass[tikz,border=10pt]{article}
%\usepackage{tikz}
%\usetikzlibrary{positioning}
%\begin{document}

\newcommand{\vet}[1]{\foreach \num in {#1}{\el{\num}}}
\newcommand{\el}[1]{\tikz{\node[font=\footnotesize, minimum size=16pt, draw]{#1}}}
\newcommand{\bl}{\color{blue}}
\newcommand{\gr}{\color{gray}}
\newcommand{\re}{\color{red}}
\begin{tabular}{cccc}
    """
    
    swap(arr, -1, -1)
    quicksort(arr,0, len(arr)-1)
    global TIKZ
    tikz = ""
    for i in range(len(TIKZ)//2):
        tikz += TIKZ[i][:-3] + "&" + TIKZ[i + len(TIKZ)//2 ]
    texcode += tikz +  r"""\end{tabular}"""
    _file.write(texcode)
    TIKZ = []

def runnig_example():
    gen_run([1 , 5, 8, 5,3, 2, 1], "quick-1") 
    gen_run([3 ,4,2,5,6,2,1,2,6,7,10,5], "quick-2") 
   #gen_heap([9,8,7,6,5,4,3,2,1,0.5,0.4,0.3,0.2,0.1], "tree-6" )
if __name__ == "__main__":
    runnig_example()
