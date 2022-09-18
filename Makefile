# input files
SOURCES:=title.tex abstract.tex pacs.tex body.tex authors.tex material.tex acknowledgements.tex \
         definitions.tex references.bib instructions.tex belle2-symbols.tex belle2.bst $(wildcard figures/*)

# default is note
note: note.tex $(SOURCES)
	latexmk -pdf -bibtex note

# tarball
%.paper: %.tex $(SOURCES)
	@./create_paper $@

# latex build
%: %.tex $(SOURCES)
	latexmk -pdf -bibtex $@

# removes temporary files
.PHONY : clean
clean:
	@rm -f *~ *.toc *.aux *.log *.bbl *.blg *.dvi *.tmp *.out *prlNotes.bib *.fdb_latexmk *.fls

# make word count
prlcount: 
	sed 's/{wordcount}{false}/{wordcount}{true}/' prl.tex > prl-count.tex
	$(prl-count)
	chmod +x wordcount.sh
	./wordcount.sh prl-count
	@rm wordcount.pdf prl-count*
	@echo ''
	@echo 'Figures:   Add 20+150/(aspect ratio) per figure'
	@echo 'Equations: Add 16 words per row (single column) '
	@echo 'Tables:    Add 13 words plus 6.5 words per line (single column)'
	@echo ''
	@echo 'Abstracts should also be ≤ 600 characters'
