echo "HAL query"
curl 'https://api.archives-ouvertes.fr/search/?q=title_t:%22Running%20a%20Reproducible%20Research%20Journal,%20with%20Source%20Code%20Inside%22&wt=bibtex' > limare_2012.bib

echo "arxiv query"
curl 'https://arxiv.org/abs/hep-lat/9405016' > arxiv1.bib
curl 'https://export.arxiv.org/api/query?id_list=hep-lat/9405016' > arxiv2.bib
curl 'http://export.arxiv.org/api/query?id_list=hep-lat/9405016' > arxiv3.bib
curl 'http://export.arxiv.org/api/query?search_query=ti:"Monte Carlo Methods for the Self-Avoiding Walk"&max_results=1' > arxiv4.bib
curl 'https://export.arxiv.org/api/query?search_query=hep-lat/9405016' > arxiv5.bib
