# input files
SOURCES:=title.tex abstract.tex main.tex authors.tex acknowledgements.tex definitions.tex references.bib $(wildcard figures/*)

# default is draft
draft:

# latex build
%: %.tex $(SOURCES)
	latexmk -pdf -bibtex $@
