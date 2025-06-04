from pybaseball import standings
data = standings(2016)
if isinstance(data, list) and len(data) > 4:
	print(data[4])
else:
	print("Unexpected data structure or insufficient elements in the standings.")




