###############################################################################
# Configuration Section
# This should be the only section you need to modify

# Project base filename where your main tex file is $(BASENAME).tex
BASENAME = cv

# Any supporting files needed to compile $(BASENAME).tex such as
# included tex files or figures
SUPPORTS =

# Other files that will be included in an archive
OTHER_FILES =

# Uncomment the next two lines if you wish to use bibtex.  These lines
# assume the bib file is $(BASENAME).bib.  Modify if needed.
BIBFILE = #$(BASENAME).bib
BBLFILE = #$(BASENAME).bbl

# Program locations and options
LATEX = latex
LATEXFLAGS = -interaction=nonstopmode
BIBTEX = bibtex
PDFLATEX = pdflatex
DVIPS = dvips
DVIPSFLAGS = -t letter

ACROREAD = acroread
XDVI = xdvi
GGV = ggv


###############################################################################
# File lists

DISTFILES = *.aux *.log *~ *.blg *.bbl *.dvi *.toc
CLEANFILES = $(DISTFILES) *.ps *.pdf *.zip *.tar.gz

TEMPLATE_FILES = Makefile $(BASENAME).tex

GIT_REVISION = gitrevision.tex

###############################################################################
# Build rules

all: $(BASENAME).dvi $(BASENAME).ps $(BASENAME).pdf

preview: $(BASENAME).dvi
	$(XDVI) $(BASENAME).dvi &

$(BASENAME).aux: $(BASENAME).tex $(SUPPORTS) $(BIBFILE)
	$(LATEX) $(LATEXFLAGS) $(BASENAME).tex

$(BASENAME).bbl: $(BASENAME).tex $(BIBFILE) $(BASENAME).aux
	$(BIBTEX) $(BASENAME).aux

$(BASENAME).dvi: $(BASENAME).tex $(BASENAME).aux $(BBLFILE) $(BIBFILE) $(GIT_REVISION)
	$(LATEX) $(LATEXFLAGS) $(BASENAME).tex
	$(LATEX) $(LATEXFLAGS) $(BASENAME).tex

$(BASENAME).ps: $(BASENAME).dvi $(GIT_REVISION)
	$(DVIPS) $(BASENAME).dvi -o $@ $(DVIPSFLAGS)

$(BASENAME).pdf: $(BASENAME).tex $(GIT_REVISION) #$(BASENAME).aux $(BIBFILE) $(BBLFILE)
	pdflatex -interaction=nonstopmode $(BASENAME).tex

###############################################################################
# Clean-up rules

clean:
	-rm -f $(CLEANFILES)

distclean:
	-rm -f $(DISTFILES)

