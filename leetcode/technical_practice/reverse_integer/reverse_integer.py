def reverse(self, x: int) -> int:
    str_int = str(x)

    if str_int[0] != '-':
        return int(str_int[::-1]) if int(str_int[::-1]) < 2**31 else 0
    
    else:
        str_int = str_int[1:]
        
        return int('-' + str_int[::-1]) if int('-' + str_int[::-1]) > -2**31 else 0
