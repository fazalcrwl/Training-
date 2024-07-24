def numb(num):

    if num<0:
        return False

    else:
        z=str(num)
        z=z[::-1]
        z=int(z)
        if z== num:
            return True
        else:
            return False
