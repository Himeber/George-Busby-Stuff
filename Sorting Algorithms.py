import time
from random import choice
def strandstatus(main,mid,sol,digit):
    print("Main list: " + str(main))
    print("Mid list: " + str(mid))
    print("Solution list: " + str(sol))
    print("Digit: " + str(digit))
def strandsort(mainlist):
    runtime = 0
    pos = 0
    notsorted = True
    digit = None
    midlist = []
    sollist = []
    strt=time.perf_counter_ns()
    while notsorted:
        digit = mainlist[0]
        midlist.append(digit)
        print("added " + str(digit) + " to mid")
        mainlist = mainlist[1:]
        print("deleted " + str(digit) + " from main")
        for i in mainlist:
            if i >= digit:
                midlist.append(i)
                print("added " + str(i) + " to mid")
                mainlist = mainlist[0:pos:]
                print("deleted " + str(i) + " from main")
                strandstatus(mainlist,midlist,sollist,digit)
            pos += 1 
        for i in midlist:
            sollist.append(i)
            print("added " + str(i) + " to solution list")
        midlist = []
        print("cleared midlist")
        if mainlist == []:
            notsorted = False
    return sollist

def sortBitonically(lst):
    #[#inPair,#step,"what each step does"]
    s2=[[2,1,"S"]]
    s4=[[2,1,"SB"],[4,2,"SS"],[2,1,"SS"],]
    s8=[[2,1,"SBSB"],[4,2,"SSBB"],[2,1,"SSBB"],"You have now made a bitonic sequence!",[8,4,"SSSS"],[4,2,"SSSS"],[2,1,"SSSS"]]
    s16=[[2,1,"SBSBSBSB"],[4,2,"SSBBSSBB"],[2,1,"SSBBSSBB"],[8,4,"SSSSBBBB"],[4,2,"SSSSBBBB"],[2,1,"SSSSBBBB"],"doner",[16,8,"SSSSSSSS"],[8,4,"SSSSSSSS"],[4,2,"SSSSSSSS"],[2,1,"SSSSSSSS"]]#[2,1,"SSSSSSSS"],
    s32=[[2,1,"SB"*8],[4,2,"SSBB"*4],[2,1,"SSBB"*4],[8,4,"SSSSBBBB"*2],[4,2,"SSSSBBBB"*2],[2,1,"SSSSBBBB"*2],[16,8,"SSSSSSSSBBBBBBBB"*1],[8,4,"SSSSSSSSBBBBBBBB"*1],[4,2,"SSSSSSSSBBBBBBBB"*1],[2,1,"SSSSSSSSBBBBBBBB"*1],"Done",[16,8,"S"*16],[8,4,"S"*16],[4,2,"S"*16],[2,1,"S"*16]]
    if len(lst)==2:
        stg=s2.copy()
    elif len(lst)==4:
        stg=s4.copy()
    elif len(lst)==8:
        stg=s8.copy()
    elif len(lst)==16:
        stg=s16.copy()
    elif len(lst)==32:
        stg=s32.copy()
    strt=time.perf_counter_ns()
    for i in stg:
        if type(i)is str or i[0]>len(lst):
            print(i)
            print(lst)
            continue
        b=[]
        for j in range(0,len(lst),i[0]):
            b.append(lst[j:j+i[0]])
        stp=0
        for j in range(len(b)):
            for k in range(0,int(len(b[j])/2)):
                mode=i[2][stp]
                n1,n2=b[j][k],b[j][k+i[1]]
                if mode=="S":
                    n1,n2=min(n1,n2),max(n1,n2)
                else:
                    n1,n2=max(n1,n2),min(n1,n2)
                b[j][k],b[j][k+i[1]]=n1,n2
                stp+=1
        lst=[]
        for k in b:
            for j in k:
                lst.append(j)
    end=time.perf_counter_ns()
    return (lst,strt,end,end-strt)
def genLst(leng):
    lst=[_ for _ in range(leng)]
    lst2=[]
    for i in range(len(lst)):
        ch=choice(lst)
        lst.remove(ch)
        lst2.append(ch)
    return lst2
while True:
    print("1. Bitonic\n2. Bubble\n3. Strand")
    tp=input("What algorithim would you like to use? ")
    match tp:
        case "1":
            dor=input("Would you like to generate a list? (y/n) ")
            lst=[]
            if dor=="y":
                for i in range(8):
                    lst.append(int(input("num 1-8: ")))
            else:
                lst=genLst(8).copy()
            print("Starting list:",lst)
            bil,bis,bie,bise=sortBitonically(lst)
            print("The sorted list is:",bil)
            print("It took",bise/1000000,"milliseconds! Isn't that speed!")
        case "2":
            print("Hey chat")
        case _:
            print("ERROR! That aint right enough!")
            break