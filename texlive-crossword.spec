%global tl_name crossword
%global tl_revision 79069

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.17
Release:	%{tl_revision}.1
Summary:	Typeset crossword puzzles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gene/crossword
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/crossword.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/crossword.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/crossword.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An extended grid-based puzzle package, designed to take all input (both
grid and clues) from the same file. The package can typeset grids with
holes in them (for advertisements, or other sorts of stuff), and can
deal with several sorts of puzzle: The classical puzzle contains numbers
for the words and clues for the words to be filled in. The numbered
puzzle contains numbers in each cell where identical numbers represent
identical letters. The goal is to find out which number corresponds to
which letter. The fill-in type of puzzle consists of a grid and a list
of words. The goal is to place all words in the grid. Sudoku and Kakuro
puzzles involve filling in grids of numbers according to their own
rules. Format may be block-separated, or separated by thick lines. Input
to the package is somewhat redundant: specification of the grid is
separate from specification of the clues (if they are necessary). The
author considers this style both 'natural' and robust.

