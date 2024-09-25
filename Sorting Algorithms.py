#chatboard
#weeeeeeeeee
#
import time
from random import choice
def strandmerge(thing,thing2,step):
    returner = []
    pos = 0
    while True:
        if thing[pos]:
            thingval = thing[pos]
        else:
            thingval = None
        if step:
            print("List 1 value: " + str(thingval))
        if thing2[pos]:
            thing2val = thing2[pos]
        else:
            thing2val = None
        if step:
            print("List 1 value: " + str(thingval))
        if thingval or thing2val:
            try:
                if thingval > thing2val:
                    returner.append(thing2val)
                    if step:
                        print("Added " + str(thing2val) + " to merge list")
                elif thing2val > thingval:
                    returner.append(thingval)
                    if step:
                        print("Added " + str(thingval) + " to merge list")
                else:
                    returner.append(thingval)
                    if step:
                        print("Added " + str(thingval) + " to merge list")
            except:
                print("ERROR")
        else:
            return(returner)
def strandstatus(main,mid,sol,digit):
    print("Main list: " + str(main))
    print("Mid list: " + str(mid))
    print("Solution list: " + str(sol))
    print("Digit: " + str(digit))
def strandSort(mainlist,step):
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
        if step:
            print("added " + str(digit) + " to mid")
        mainlist = mainlist[1:]
        if step:
            print("deleted " + str(digit) + " from main")
        for i in mainlist:
            if i >= digit:
                midlist.append(i)
                if step:
                    print("added " + str(i) + " to mid")
                mainlist = mainlist[0:pos:]
                if step:
                    print("deleted " + str(i) + " from main")
                strandstatus(mainlist,midlist,sollist,digit)
            pos += 1 
        for i in midlist:
            sollist = strandmerge(midlist,sollist,step)
        midlist = []
        if step:
            print("cleared midlist")
        if mainlist == []:
            notsorted = False
    end=time.perf_counter_ns()
    return (sollist,strt,end,end-strt)
#strand sort ends here

def sortBitonically(lst,step):
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
            if step:
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
                    if step:
                        print("We do SU on",n1,"and",n2)
                    n1,n2=min(n1,n2),max(n1,n2)
                else:
                    if step:
                        print("We do BU on",n1,"and",n2)
                    n1,n2=max(n1,n2),min(n1,n2)
                b[j][k],b[j][k+i[1]]=n1,n2
                stp+=1
        lst=[]
        for k in b:
            for j in k:
                lst.append(j)
    end=time.perf_counter_ns()
    return (lst,strt,end,end-strt)

def bubbleSort(list,step):
    n=len(list)
    strt=time.perf_counter_ns()
    for i in range(n):
        swap=False
        for j in range( 0,n-i-1):
            if step:
                print("We check if",list[j],"is bigger than",list[j+1])
            time.sleep(0.1)
            if list[j]>list[j+1]:
                if step:
                    print(list[j],"is bigger than",list[j+1])
                time.sleep(0.1)
                list[j], list[j+1] = list[j+1], list[j]
                if step:
                    print("we have swapped the two values")
                time.sleep(0.1)
                swap=True
            else:
                if step:
                    print(list[j],"is not bigger than",list[j+1])
                time.sleep(0.1)
                if step:
                    print("we don't swap them")
                time.sleep(0.1)
        if (swap == False):
            break
    end=time.perf_counter_ns()
    return (list,strt,end,end-strt)
    
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
    stp=input("Would you like to see every step? This affects porformance and readability so... (y/n) ")
    if tp in ["1","2","3"]:
        if stp=="y":
            stp=True
        else:
            stp=False
        dor=input("Would you like to generate a list? (y/n) ")
        lst=[]
        if dor=="y":
            for i in range(8):
                lst.append(int(input("num 1-8: ")))
        else:
            lst=genLst(8).copy()
        print("Starting list:",lst)
        match tp:
            case "1":
                sortList,sortStart,sortEnd,sortLen=sortBitonically(lst,stp)
            case "2":
                sortList,sortStart,sortEnd,sortLen=bubbleSort(lst,stp)
            case "3":
                sortList,sortStart,sortEnd,sortLen=strandSort(lst,stp)
            case _:
                print("ERROR! That aint right enough!")
                break
        print("The sorted list is:",sortList)
        print("It took",sortLen/1000000,"milliseconds! Isn't that speed!")
    
