book_pages = int(input())
pages_for_hour = int(input())
days_for_book = int(input())
time = book_pages // pages_for_hour
hours_needed = time // days_for_book
print(hours_needed)
