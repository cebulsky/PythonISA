text = "Python is a fantastic snake"
how_many_chars = len(text)

list_of_indexes = range(0,how_many_chars,2)

for idx in list_of_indexes:
    print(text[idx], end="")

# TODO
print("\n\n")

months = ["Jan", "Feb", "March"]

for idx, month in enumerate(months):
    print(f"Na indexie {idx}: wartosc: {month}")
