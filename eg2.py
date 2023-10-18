import scholarly

search_query = scholarly.search_pubs('PhysiCell: An open source physics-based cell simulator for 3-D multicellular systems')
scholarly.pprint(next(search_query))
