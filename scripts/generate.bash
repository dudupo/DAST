#!/bin/bash

mkdir "weeks"
for i in {00..15}
do
	# echo "$i"
	mkdir "weeks/week-$i"
	# echo "" > tex/exercises/exe-$i.tex
	# echo "" > tex/lectures-TA/lec-$i.tex 
	# echo "" > tex/solutions/sol-$i.tex
	ln tex/exercises/exe-$i.tex weeks/week-$i/exe-$i.tex 
	ln tex/lectures-TA/lec-$i.tex weeks/week-$i/lec-$i.tex 
	ln tex/solutions/sol-$i.tex weeks/week-$i/sol-$i.tex 
done
