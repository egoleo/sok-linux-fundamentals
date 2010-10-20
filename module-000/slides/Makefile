SHELL = /bin/sh

all: sok.pdf course.pdf

sok.pdf: sok.tex
	pdflatex sok.tex

course.pdf: course.tex
	pdflatex course.tex

clean:
	rm -f *aux *log *nav *out *snm *toc

distclean: clean
	rm -f *pdf

