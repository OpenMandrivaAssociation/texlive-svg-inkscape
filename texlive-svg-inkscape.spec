# revision 19788
# category Package
# catalog-ctan /info/svg-inkscape
# catalog-date 2010-09-08 12:29:06 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-svg-inkscape
Version:	20100908
Release:	1
Summary:	How to include an SVG image in LaTeX using Inkscape
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/svg-inkscape
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svg-inkscape.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svg-inkscape.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The document demonstrates the use of SVG imainges in LaTeX
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
