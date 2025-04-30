size_disk_mb = 1.44  # Мб
pages_in_book = 100
lines_of_pages = 50
token_lines = 25
size_token = 4  # байта

size_disk_b = size_disk_mb * 1024 ** 2
size_book = pages_in_book * lines_of_pages * token_lines * size_token
max_book_in_disk = size_disk_b // size_book

print(f"Количество книг, помещающихся на дискету: {(max_book_in_disk):.0f}")
