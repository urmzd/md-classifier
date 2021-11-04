#!/usr/bin/bash

# Install dependencies.
sudo apt-get install -y bibtex pdflatex texlive-full

# Change directories
cd docs

# Save current directory
wd=$(pwd) 

function compile-latex {
  # Go to directory with .tex
  cwd = $(dirname "$2")
  cd $cwd

  texs=( *.tex )
  _bibs=( *.bib )
  bibs="${_bibs[@]%%.*}"

  # compilation
  for tex in ${tex[@]}; do
    pdflatex tex
  done

  for bib in ${bib[@]}; do
    bibtex bib 
  done

  for tex in ${tex[@]}; do
    pdflatex tex
  done

  for tex in ${tex[@]}; do
    pdflatex tex
  done

  pdfs=( *.pdf )

  for pdf in ${pdfs[@]}; do
    cp pdf cwd
  done
  
  # Go back home
  cd $1
}

# Compile all docs for all tex files
find docs -name '*.pdf' | while read file; do compile-latex $wd $file; done
