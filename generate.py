with open("artifact.txt", "w") as f:
	for i in range(1, 100_000, 10):
		print(i, file=f)
