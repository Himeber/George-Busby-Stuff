def strandsort(mainlist):
    runtime = 0
    notsorted = True
    digit = None
    midlist = []
    sollist = []
    while notsorted:
        digit = mainlist[0]
        midlist.append(digit)
        mainlist = mainlist[1:]
        for i in mainlist:
            if i <= digit:
                midlist.append(i)
                mainlist = mainlist - i
        for i in midlist:
            sollist.append(i)
        midlist = []
        if mainlist == []:
            notsorted = False
    return sollist
