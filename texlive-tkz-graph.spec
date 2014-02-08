# revision 22832
# category Package
# catalog-ctan /macros/latex/contrib/tkz/tkz-graph
# catalog-date 2011-06-06 00:03:44 +0200
# catalog-license lppl
# catalog-version 1.00
Name:		texlive-tkz-graph
Version:	1.00
Release:	3
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

%description
The package is designed to create graph diagrams as simply as
possible, using TikZ.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.00-2
+ Revision: 756979
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.00-1
+ Revision: 719765
- texlive-tkz-graph
- texlive-tkz-graph
- texlive-tkz-graph

