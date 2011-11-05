# revision 22832
# category Package
# catalog-ctan /macros/latex/contrib/tkz/tkz-graph
# catalog-date 2011-06-06 00:03:44 +0200
# catalog-license lppl
# catalog-version 1.00
Name:		texlive-tkz-graph
Version:	1.00
Release:	1
Summary:	Draw graph-theory graphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tkz/tkz-graph
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-graph.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-graph.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package is designed to create graph diagrams as simply as
possible, using TikZ.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tkz-graph/tkz-graph.sty
%doc %{_texmfdistdir}/doc/latex/tkz-graph/latex/TKZdoc-gr-Dijkstra.tex
%doc %{_texmfdistdir}/doc/latex/tkz-graph/latex/TKZdoc-gr-Welsh.tex
%doc %{_texmfdistdir}/doc/latex/tkz-graph/latex/TKZdoc-gr-annales.tex
%doc %{_texmfdistdir}/doc/latex/tkz-graph/latex/TKZdoc-gr-couverture.tex
%doc %{_texmfdistdir}/doc/latex/tkz-graph/latex/TKZdoc-gr-edge.tex
%doc %{_texmfdistdir}/doc/latex/tkz-graph/latex/TKZdoc-gr-installation.tex
%doc %{_texmfdistdir}/doc/latex/tkz-graph/latex/TKZdoc-gr-label.tex
%doc %{_texmfdistdir}/doc/latex/tkz-graph/latex/TKZdoc-gr-main.tex
%doc %{_texmfdistdir}/doc/latex/tkz-graph/latex/TKZdoc-gr-presentation.tex
%doc %{_texmfdistdir}/doc/latex/tkz-graph/latex/TKZdoc-gr-prob.tex
%doc %{_texmfdistdir}/doc/latex/tkz-graph/latex/TKZdoc-gr-style.tex
%doc %{_texmfdistdir}/doc/latex/tkz-graph/latex/TKZdoc-gr-vertex.tex
%doc %{_texmfdistdir}/doc/latex/tkz-graph/latex/TKZdoc-gr-vertices.tex
%doc %{_texmfdistdir}/doc/latex/tkz-graph/latex/graph.ist
%doc %{_texmfdistdir}/doc/latex/tkz-graph/readme-tkz-graph.txt
%doc %{_texmfdistdir}/doc/latex/tkz-graph/tkz-graph-screen.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
