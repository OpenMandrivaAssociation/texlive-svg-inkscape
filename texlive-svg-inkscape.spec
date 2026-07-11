%global tl_name svg-inkscape
%global tl_revision 32199

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	How to include an SVG image in LaTeX using Inkscape
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/svg-inkscape
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svg-inkscape.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svg-inkscape.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The document demonstrates the use of SVG images in LaTeX documents.
Using the "PDF+LaTeX output" option of Inkscape, it is possible to
include SVG in documents, in which LaTeX typesets the text. This results
in uniform text style throughout the document, including text in images;
moreover, LaTeX commands may be used in the image's text, providing such
things as mathematics and references. The document also describes how to
automate the conversion from SVG to PDF+LaTeX using Inkscape.

