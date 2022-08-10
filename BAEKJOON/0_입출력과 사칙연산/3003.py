pieces = list(map(int, input().split()))
correct = [1, 1, 2, 2, 2, 8]

zip_pieces = zip(pieces, correct)

for p, c in zip_pieces:
  print(c - p, end=' ')
