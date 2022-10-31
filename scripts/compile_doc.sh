#!/bin/sh
pdflatex  --shell-escape $1
filename=`basename $1 .tex`
biber $filename
pdflatex  --shell-escape $1

# change to your local directory.  
rootpath="~/workspace/DAST"

mv $filename.pdf "$rootpath/pdfs/"  

if [ ! -d "./logs" ]; then
 mkdir "./logs"
fi

for ext in aux bcf log run.xml bbl blg tex.bbl tex.blg; do 
 mv $filename.$ext ./logs/
done

Date=`date`
git add $filename.tex  "$rootpath/pdfs/$filename.pdf"
git commit -m "compiling $filenaem-$Date"
