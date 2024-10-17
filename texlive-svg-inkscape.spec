Name:		texlive-svg-inkscape
Version:	32199
Release:	2
Summary:	How to include an SVG image in LaTeX using Inkscape
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/svg-inkscape
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svg-inkscape.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svg-inkscape.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The document demonstrates the use of SVG images in LaTeX
documents. Using the "PDF+LaTeX output" option of Inkscape, it
is possible to include SVG in documents, in which LaTeX
typesets the text. This results in uniform text style
throughout the document, including text in images; moreover,
LaTeX commands may be used in the image's text, providing such
things as mathematics and references. The document also
describes how to automate the conversion from SVG to PDF+LaTeX
using Inkscape.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/svg-inkscape/InkscapePDFLaTeX.pdf
%doc %{_texmfdistdir}/doc/latex/svg-inkscape/InkscapePDFLaTeX.tex
%doc %{_texmfdistdir}/doc/latex/svg-inkscape/README
%doc %{_texmfdistdir}/doc/latex/svg-inkscape/image-normal.pdf
%doc %{_texmfdistdir}/doc/latex/svg-inkscape/image.pdf
%doc %{_texmfdistdir}/doc/latex/svg-inkscape/image.pdf_tex
%doc %{_texmfdistdir}/doc/latex/svg-inkscape/image.svg

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
