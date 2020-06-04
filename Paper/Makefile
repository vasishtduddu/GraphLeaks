PAPERNAME=paper
TEXFILES =  *.tex *.bib *.sty

all:
	pdflatex $(PAPERNAME)
	bibtex $(PAPERNAME)
	pdflatex $(PAPERNAME)
	pdflatex $(PAPERNAME)
clean:
	rm -f *.ps $(PAPERNAME).pdf *.dvi *.txt *.aux *.log *.blg *.bbl *~ *.ilg *.idx *.out *.in
