<%doc>
cv-us.tex
$Id: cv-us.tex,v 1.28 2006/12/12 22:53:52 jrblevin Exp $

LaTeX Curriculum Vitae Template

Copyright (C) 2004-2006 Jason Blevins

You may use use this document as a template to create your own CV
and you may redistribute the source code freely. No attribution is
required in any resulting documents, however, I do ask that you
please leave this notice and the above URL in the source code if you
choose to redistribute this file.

Jason R. Blevins <jrblevin@sdf.lonestar.org>
http://jrblevin.freeshell.org
Durham, December 12, 2006

---------------------------------------------------------------------------

Notes:

* Don't forget to change `pdfauthor' and `keywords' in the \hypersetup
  section below.

* To create a new page use: \newpage \opening

* res.cls includes an \address{} command which can be used up to twice,
  but my address is too long for the format it uses.

* Alternate documentclass statement to put headings in margin:
  \documentclass[margin,line,11pt,final]{res}

* Can divide publication/presentation list into subsections by year:
  \section{\bf\small\hspace{8mm}2006}

----------------------------------------------------------------------------
</%doc>

\documentclass[overlapped,line,letterpaper]{res}

\usepackage{ifpdf}
\usepackage{cs-cv}

\ifpdf
  \usepackage[pdftex]{hyperref}
\else
  \usepackage[hypertex]{hyperref}
\fi

\usepackage{tabulary}

\hypersetup{
  letterpaper,
  colorlinks,
  urlcolor=black,
  pdfpagemode=none,
  pdftitle={Curriculum Vitae},
  pdfauthor={${cv.basics.name}},
  pdfcreator={$ $Id: cv-us.tex,v 1.28 2006/12/12 22:53:52 cscutcher Exp $ $},
  pdfsubject={Curriculum Vitae},
  pdfkeywords={ ${" ".join(cv.get_keywords_iter())} }
}

##%%===========================================================================%%

\begin{document}

##%---------------------------------------------------------------------------
##% Document Specific Customizations

##% Make lists without bullets and with no indentation
\setlength{\leftmargini}{0em}
\setlength{\leftmargin}{1.5cm}
\setlength{\rightmargin}{1.5cm}
\setlength{\textheight}{800pt}
\setlength{\voffset}{-0.5in}
\renewcommand{\labelitemi}{}

##% Use large bold font for printed name at top of pages
\renewcommand{\namefont}{\large\textbf}

##%---------------------------------------------------------------------------

\name{${cv.basics.name}}

\begin{resume}

\begin{ncolumn}{2}
  Phone: ${cv.basics.phone}                \\
  {\tt ${cv.basics.email}}  & {\tt \verb+${cv.basics.website}+}
\end{ncolumn}

##%---------------------------------------------------------------------------

\section{\bf Education}
% for education in cv.education:
${education.area} - ${education.studyType} \\
${education.institution} [${education.endDate.year}]
% endfor

##%---------------------------------------------------------------------------
##% \begin{format}
##% \title{l}\dates{r}\\
##% \employer{l}\location{r}\\
##% \body\\
##% \end{format}

\section{\bf Employment}
% for job in cv.work:
\csposition{${job.company}}{${job.position}}{${job.startDate.year} - ${job.endDate.year if "endDate" in job else "present"}}
{
    ${job.summary}
    % if "highlights" in job:
        \begin{itemize}
        % for highlight in job.highlights:
        \item ${highlight}
        % endfor
        \end{itemize}
    % endif
}

% endfor


\section{\bf{Technology Experience} }
% for skill_section in cv.skills:
\subsection{${skill_section.name}}
\begin{itemize}
    % for keyword in skill_section.keywords:
    \item ${keyword}
    % endfor
\end{itemize}
% endfor

\section{\bf{Interests} }
\begin{itemize}
% for interests in cv.interests:
% for keyword in interests.keywords:
\item ${keyword}
% endfor
% endfor

\end{itemize}

\begin{center}
    {\tiny \rm $ $Date: \today  }
\end{center}

\end{resume}

\end{document}
