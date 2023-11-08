def bsearch(spisok, left, right, val):
    if (right < left):
        return None
    else:
        midval = left + ((right - left) // 2)


        if spisok[midval] > val:
            return bsearch(spisok, left, midval - 1, val)
        elif spisok[midval] < val:
            return bsearch(spisok, midval + 1, right, val)
        else:
            return midval


spisok = [1, 6, 3, 5, 11, 19, 24]
print(bsearch(spisok, 0, len(spisok), 5))
print(bsearch(spisok,0, len(spisok), 0))