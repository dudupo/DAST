#!/bin/bash 
given_file=`basename $1 .pdf` 
output_file=$2

convert "$given_file.pdf" -magnify --adaptive-sharpen  "$given_file.png" 

if [[ -f "$given_file.txt" ]]; then 
  rm "$given_file.txt"
fi
echo "" > tempfile
for photo in $given_file-*.png; do 
  tesseract $photo tempfile 
  cat tempfile.txt >> "$given_file.txt" 
  rm tempfile.txt  
done

# rm $given_file-*.png 
cat header.template   >> "$given_file.tex"
cat "$given_file.txt" >> "$given_file.tex"
cat clouse.template   >> "$given_file.tex"
mv "$given_file.tex" "../tex/sandbox/$output_file.tex"
rm "$given_file.txt" 

