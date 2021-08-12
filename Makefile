# input files
SOURCES:=title.tex abstract.tex pacs.tex main.tex authors.tex material.tex acknowledgements.tex definitions.tex references.bib $(wildcard figures/*)

# default is note
note:

# tarball
%.paper: %.tex $(SOURCES)
	@./create_paper $@


# latex build
%: %.tex $(SOURCES)
	latexmk -pdf -bibtex $@
