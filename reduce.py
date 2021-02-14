import pickle
with open('./data3.pkl', 'rb') as f:
    total = pickle.load(f)
for item in total:
	print(len(item))
total_reduced = []
cut = []
total_reduced.append(total[0][0:900000])
cut.append(total[0][900000:-1])
total_reduced.append(total[1][0:30000])
cut.append(total[1][30000:-1])
total_reduced.append(total[2][0:500000])
cut.append(total[2][500000:-1])
total_reduced.append(total[3][0:375000])
cut.append(total[3][375000:-1])
total_reduced.append(total[4][0:300000])
cut.append(total[4][300000:-1])
total_reduced.append(total[5][0:700000])
cut.append(total[5][700000:-1])

for item in total_reduced:
	print(len(item))

pickle.dump(total_reduced, open( "reduced_data3.pkl", "wb+" ) )
pickle.dump(cut, open("testing_data3.pkl", "wb+"))
