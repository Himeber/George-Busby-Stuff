#chatboard
#weeeeeeeeee
#kljhds kjds; dsakjg dsg jj gjs gkaks gk ds g gksa g kg g noyes
import time
from math import floor,ceil,log2
from random import choice,randint
def strandmerge(thing,thing2,step):
    returner = []
    count1 = 0
    count2 = 0
    if step:
        print("Merging mid and endlists")
    while count1 < len(thing) and count2 < len(thing2):
        if thing[count1] <= thing2[count2]:
            if step:
                print("Added " + str(thing[count1]) + " to merged list")
            returner.append(thing[count1])
            count1 += 1
        else:
            if step:
                print("Added " + str(thing2[count2]) + " to merged list")
            returner.append(thing2[count2])
            count2 += 1
    returner.extend(thing[count1:])
    returner.extend(thing2[count2:])
    if step:
        print("Set endlist to mergedlist")
    return returner
def strandSort(mainlist,step):
    midlist = []
    sollist = []
    strt=time.perf_counter_ns()
    while mainlist:
        midlist = [mainlist.pop(0)]
        if step:
            print("Moved " + str(midlist[-1]) + " from main to mid")
        counter = 0
        while counter < len(mainlist):
            if midlist[-1] < mainlist[counter]:
                midlist.append(mainlist.pop(counter))
                if step:
                    print("Moved " + str(midlist[-1]) + " from main to mid")
            else:
                counter += 1
        sollist = strandmerge(sollist,midlist,step)
    end=time.perf_counter_ns()
    return (sollist,strt,end,end-strt)
#strand sort ends here
def compare_and_swap(a, i, j, direction):
    if (direction == 1 and a[i] > a[j]) or (direction == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]

def bitonic_merge(a, low, count, direction):
    if count > 1:
        k = count // 2
        for i in range(low, low + k):
            compare_and_swap(a, i, i + k, direction)
        bitonic_merge(a, low, k, direction)
        bitonic_merge(a, low + k, k, direction)

def bitonic_sort(a, low, count, direction):
    if count > 1:
        k = count // 2
        bitonic_sort(a, low, k, 1)
        bitonic_sort(a, low + k, k, 0)
        bitonic_merge(a, low, count, direction)
    return a

def run(a, direction=1):
    strt=time.perf_counter_ns()
    lst=bitonic_sort(a, 0, len(a), direction)
    end=time.perf_counter_ns()
    # print()
    return (lst,strt,end,end-strt)
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
                    print("we don't swap them")
                    time.sleep(0.1)
        if (swap == False):
            break
    end=time.perf_counter_ns()
    return (list,strt,end,end-strt)
    
def insertionSort(list,step):
    strt=time.perf_counter_ns()
    for i in range(1, len(list)):
        n = list[i]
        j = i - 1
        if step:
            print("we check if",n,"is smaller than",list[j])
            time.sleep(0.1)
        while j >= 0 and n < list[j]:
            if step:
                print(n,"is smaller than",list[j],"so we move it one to the left")
                time.sleep(0.1)
            list[j + 1] = list[j]
            j -= 1
            if step:
                print("we check if",n,"is smaller than",list[j])
                time.sleep(0.1)
        if step:
            print(n,"is not smaller than",list[j],"so it stays put")
            time.sleep(0.1)
        list[j + 1] = n
    end=time.perf_counter_ns()
    if step:
        print("it is sorted and therefore is funi")
        time.sleep(0.1)
    return (list,strt,end,end-strt)

def genLst(leng):
    # lst=[_ for _ in range(leng)]
    lst2=[]
    for i in range(leng):
        ch=randint(-leng,leng*2)
        # lst.remove(ch)
        lst2.append(ch)
    return lst2

while True:
    print("1. Bitonic\n2. Bubble\n3. Strand\n4. Insertion")
    tp=input("What algorithim would you like to use? ")
    if tp=="quit":
        quit(2)
    if tp in ["1","2","3","4"]:
        stp=input("Would you like to see every step? This affects porformance and readability so... (y/n) ")
        if stp=="y":
            stp=True
        else:
            stp=False
        dor=input("Would you like to generate a list? (y/n) ")
        ln=int(input("How long is this list? "))
        # if tp=="1" and ln>16:
        #     ln=16
        lst=[]
        if dor=="y":
            for i in range(ln):
                lst.append(int(input("num 1-8: ")))
        else:
            lst=genLst(ln).copy()
        if tp=="1":
            # mnE=floor(log2(ln))
            mxE=ceil(log2(ln))
            # print(mnE,mxE)
            nds=(2**mxE)-ln
            # print(nds,mnE,mxE,log2(ln),log2(8),log2(16))
            # quit(1)
            for i in range(0,nds):
                lst.append(0)
        if len(lst)<50:
            print("Starting list:",lst)
        else:
            print("Starting!")
        match tp:
            case "1":
                if len(lst)>16:
                    ooga=run(lst)
                else:
                    ooga=sortBitonically(lst,stp)
                sortList,sortStart,sortEnd,sortLen=ooga
            case "2":
                sortList,sortStart,sortEnd,sortLen=bubbleSort(lst,stp)
            case "3":
                sortList,sortStart,sortEnd,sortLen=strandSort(lst,stp)
            case "4":
                sortList,sortStart,sortEnd,sortLen=insertionSort(lst,stp)
            case _:
                print("ERROR! That aint right enough!")
                break
        if len(sortList)<50:
            print("The sorted list is:",sortList)
        print("It took",sortLen/1000000,"milliseconds! Isn't that speed!")
    else:
        print(choice(["No","That's wrong.","If you can't do this, go back to preschool!","Eat a fish.","That wasn't a possible choice!","Get a life.","Touch grass, aight!"]))
        print("You basically inputted a wronger thing.\n\n\n\n\n\n\n")