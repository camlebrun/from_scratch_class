import pandas
problem_csv_path = "/Users/camille/repo/Hetic/computer_science_basics/exercices/explorateurs/probleme_graphe_v2.csv"

problem_df = pandas.read_csv(problem_csv_path, sep=",")

noeud_depart_list = [row["noeud_amont"] for _, row in problem_df.iterrows() if row["type_aretes"] == "depart"]
noeud_arrivee_list = [row["noeud_aval"] for _, row in problem_df.iterrows() if row["type_aretes"] == "arrivee"]
association_amont_aval_dict = {row["noeud_amont"] : row["noeud_aval"] for _, row in problem_df.iterrows()}

print(association_amont_aval_dict)
for noeud_depart in noeud_depart_list:
	list_noeud_trajet = [noeud_depart]
	while not(association_amont_aval_dict[list_noeud_trajet[-1]] in noeud_arrivee_list):
		list_noeud_trajet.append(association_amont_aval_dict[list_noeud_trajet[-1]])
	list_noeud_trajet.append(association_amont_aval_dict[list_noeud_trajet[-1]])

	print(list_noeud_trajet)

