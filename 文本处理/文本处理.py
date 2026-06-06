from collections import Counter

def top_works(file_path):
    with open(file_path, "r", encoding="utf-8" ) as f:
        text = f.read()

    text = text.lower()

    works = []
    current_work = ''

    for ch in text:
        if ch.isalnum():
            current_work += ch
        else:
            if current_work:
                works.append(current_work)
                current_work = ''


    if current_work:
        works.append(current_work)

    counts = Counter(works)
    top_10 = counts.most_common(10)

    for word,count in top_10:
        print(f'{word}: {count}')


top_works("example.txt")


