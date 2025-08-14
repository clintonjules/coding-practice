def convert(self, s: str, numRows: int) -> str:
    if len(s) == 1 or numRows == 1:
        return s

    rows = [""] * numRows
    current = 0
    down = False

    for each in s:
        rows[current] += each

        if current == 0 or current == numRows-1:
            down = not down

        current += 1 if down else -1

    return "".join(rows)
