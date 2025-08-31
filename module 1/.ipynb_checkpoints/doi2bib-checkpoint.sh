#!/bin/sh
# Source: https://charly-lersteau.com/blog/2017-08-08-convert-doi-to-bib/
# Examples
# ./doi2bib.sh <DOI_list...>
# cat <file_with_DOIs> | ./doi2bib.sh, if using a pipe

if test -t 0
then input="$@"
else input="$@ `cat`"
fi
for ref in $input
do
	doi=`echo $ref | sed -e "s/^\(\(https\?:\/\/\)\?\(dx.\)\?doi.org\/\|doi:\)//"`
	wget --header="Accept: application/x-bibtex; charset=utf-8" -qO- "https://doi.org/$doi"
     # wget --header="Accept: text/x-bibliography; style=$style" -qO- "https://doi.org/$doi" to specify citation style

	echo
done
