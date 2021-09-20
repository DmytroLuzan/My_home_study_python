def triangle(row):
    row = row[:2]
    if row == 'GG':
        return 'G'
    if row == 'RR':
        return 'R'
    if row == 'BB':
        return 'B'
    if row == 'BG' or row == 'GB':
        return 'R'
    if row == 'RG' or row == 'GR':
        return 'B'
    if row == 'BR' or row == 'RB':
        return 'G'
    if len(row) == 1:
        return row
