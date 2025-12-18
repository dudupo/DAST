#!/bin/bash

#../../scripts/compile_doc.sh ./lec-00-peaks.tex 
#../../scripts/compile_doc.sh ./lec-master_and_linear_sorts.tex 
cd ../../DAST-private/lyx/ 
../../scripts/compile_doc.sh ./ex0-2024.tex 
../../scripts/compile_doc.sh ./ex0-2024-sol.tex
mv ../../pdfs/ex0-2024.pdf  ../../pdfs/ex0-2025.pdf 
mv  ../../pdfs/ex0-2024-sol.pdf ../../pdfs/ex0-2025-sol.pdf
cd ../../tex/lectures-TA/ 

#
#../../scripts/compile_doc.sh ./lec-hashing.tex
#../../scripts/compile_doc.sh ./lec-heaps.tex
