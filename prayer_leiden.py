import itertools
from itertools import combinations


def all_combinations(texts_list, n):
    all_combinations = []
    texts = combinations(texts_list, n)
    for t in texts:
        all_combinations.append(sorted(list(t)))
    return(all_combinations)

def all_frequent_combinations(texts_list, n):
    all_combinations = []
    texts = combinations(texts_list, n)
    for t in texts:
        books = find_books_containing_cluster(t,book_texts)
        if len(books)>2:
            all_combinations.append(sorted(list(t)))
    return(all_combinations)
        
def intersection(list1,list2):
    intersection = list(set(list1) & set(list2))
    return intersection

def deduplicate_list(l):
    l.sort()
    return list(l for l,_ in itertools.groupby(l))

def remove_subsets(clusters):
    return [x for x in clusters if not any(set(x)<=set(y) for y in clusters if x is not y)]

def find_text_frequency(text,book_texts):
    freq = 0
    for book in book_texts:
        if text in book_texts[book]:
            freq += 1
    return freq

def find_books_containing_cluster(cluster,book_texts):
    books = []
    for book in book_texts:
        texts = book_texts[book]
        if len(intersection(texts,cluster))==len(cluster):
            books.append(book)
    return books