from scholarly import scholarly
# from habanero import Crossref

# from scholarly import ProxyGenerator

# Set up a ProxyGenerator object to use free proxies
# This needs to be done only once per session
# pg = ProxyGenerator()
# pg.FreeProxies()
# scholarly.use_proxy(pg)


# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author('Paul Macklin')
author = scholarly.fill(next(search_query))
# print(author)

# Print the titles of the author's publications
#print([pub['bib']['title'] for pub in author['publications']])
fout = open("pc_cite.csv", 'w')
# cr = Crossref()
for pub in author['publications']:
    # if 'PhysiCell' in pub['bib']['title']:
    if 'Physics-Based Cell Simulator' in pub['bib']['title']:
        print(pub['bib']['title'])
        print("\n-----")
        idx = 0
        for citation in scholarly.citedby(pub):
            idx += 1
            print(f"{idx}) {citation['bib']['title']}")
            # result = cr.works(query = 'An Evaluation of the Biological and Toxicological Properties of Aloe Barbadensis (Miller), Aloe Vera')
            # result = cr.works(query = citation['bib']['title'])
            # doi = result['message']['items'][0]['DOI']
            # print(doi)
            # https://scholar.google.com/scholar?q=10.1038/s41524-020-00366-8&hl=en&as_sdt=0&as_vis=1&oi=scholart
            if idx > 999:
                break
            if citation['pub_url'] is not None:
                fout.write(f"{idx};{citation['bib']['pub_year']};{citation['pub_url']};{citation['bib']['title']}" + "\n")
            else:
                fout.write(f"{idx};{citation['bib']['pub_year']};NA;{citation['bib']['title']}" + "\n")
        break
fout.close()

# Take a closer look at the first publication
# pub = scholarly.fill(author['publications'][0])
#print(pub)

# print(pub['bib'])

# -->
# {'title': 'Nonlinear modelling of cancer: bridging the gap between cells and tumours',
#  'pub_year': 2009,
#  'citation': 'Nonlinearity 23 (1), R1, 2009',
#  'author': 'John S Lowengrub and Hermann B Frieboes and Fang Jin and Yao-Li Chuang and Xiangrong Li and Paul Macklin and Steven M Wise and Vittorio Cristini',
#  'journal': 'Nonlinearity',
#  'volume': '23',
#  'number': '1',
#  'pages': 'R1',
#  'publisher': 'IOP Publishing',
#  'abstract': 'Despite major scientific, medical and technological advances over the last few decades, a cure for cancer remains elusive. The disease initiation is complex, and including initiation and avascular growth, onset of hypoxia and acidosis due to accumulation of cells beyond normal physiological conditions, inducement of angiogenesis from the surrounding vasculature, tumour vascularization and further growth, and invasion of surrounding tissue and metastasis. Although the focus historically has been to study these events through experimental and clinical observations, mathematical modelling and simulation that enable analysis at multiple time and spatial scales have also complemented these efforts. Here, we provide an overview of this multiscale modelling focusing on the growth phase of tumours and bypassing the initial stage of tumourigenesis. While we briefly review discrete modelling, our focus is on the …'}

# In [14]: pub['bib']['title']


# Which papers cited that publication?
#print([citation['bib']['title'] for citation in scholarly.citedby(pub)])
