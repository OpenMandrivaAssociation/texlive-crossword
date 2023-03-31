Name:		texlive-crossword
Version:	64375
Release:	2
Summary:	Typeset crossword puzzles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gene/crossword
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossword.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossword.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossword.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
An extended grid-based puzzle package, designed to take all
input (both grid and clues) from the same file. The package can
typeset grids with holes in them (for advertisements, or other
sorts of stuff), and can deal with several sorts of puzzle: The
classical puzzle contains numbers for the words and clues for
the words to be filled in. The numbered puzzle contains numbers
in each cell where identical numbers represent identical
letters. The goal is to find out which number corresponds to
which letter. The fill-in type of puzzle consists of a grid and
a list of words. The goal is to place all words in the grid.
Sudoku and Kakuro puzzles involve filling in grids of numbers
according to their own rules. Format may be block-separated, or
separated by thick lines. Input to the package is somewhat
redundant: specification of the grid is separate from
specification of the clues (if they're necessary). The author
considers this style both 'natural' and robust.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/crossword
%doc %{_texmfdistdir}/doc/latex/crossword
#- source
%doc %{_texmfdistdir}/source/latex/crossword

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
