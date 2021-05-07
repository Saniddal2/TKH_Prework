name_list=['bob', 'jimmy', 'max b', 'bernie', 'jordan', 'future hexdrix']
def split():
    even = []
    odd = []
    for item in name_list:
        if len(item) % 2 == 0:
            even.append(item)
        else:
            odd.append(item)

    return even, odd

split()