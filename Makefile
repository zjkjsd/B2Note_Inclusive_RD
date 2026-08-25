# input files
SOURCES:=title.tex abstract.tex body.tex $(wildcard sections/*.tex) authors.tex material.tex acknowledgements.tex \
         definitions.tex references.bib instructions.tex belle2-symbols.tex belle2.bst $(wildcard figures/*)

# default is note
note: note.tex $(SOURCES)
	latexmk -pdf -bibtex note

# latex build
%: %.tex $(SOURCES)
	latexmk -pdf -bibtex $@

# removes temporary files
.PHONY : clean
clean:
	@rm -f *~ *.toc *.aux *.log *.bbl *.blg *.dvi *.tmp *.out *prlNotes.bib *.fdb_latexmk *.fls
