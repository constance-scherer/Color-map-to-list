import matplotlib
def cmap_to_list(cmap_name, taille) : 
	cmap = matplotlib.cm.get_cmap(cmap_name) 
	liste = [] 
	for i in range(0, taille) : 
		n = i/taille liste.append(cmap(n)) 
	return liste