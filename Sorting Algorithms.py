import time
def sortBitonically(lst):
    # print(lst)
    # lst=lst.copy()
    #[#inPair,#step,"what each step does"]
    s2=[[2,1,"S"]]
    s4=[[2,1,"SB"],[4,2,"SS"],[2,1,"SS"],]
    s8=[[2,1,"SBSB"],[4,2,"SSBB"],[2,1,"SSBB"],[8,4,"SSSS"],[4,2,"SSSS"],[2,1,"SSSS"]]
    s16=[[2,1,"SBSBSBSB"],[4,2,"SSBBSSBB"],[2,1,"SSBBSSBB"],[8,4,"SSSSBBBB"],[4,2,"SSSSBBBB"],[2,1,"SSSSBBBB"],"doner",[16,8,"SSSSSSSS"],[8,4,"SSSSSSSS"],[4,2,"SSSSSSSS"],[2,1,"SSSSSSSS"]]#[2,1,"SSSSSSSS"],
    # s32=[[2,1,""],[4,2,""],[2,1,""],[8,4,""],[4,2,""],[2,1,""],[16,8,""],[8,4,""],[4,2,""],[2,1,""]]
    s32=[[2,1,"SB"*8],[4,2,"SSBB"*4],[2,1,"SSBB"*4],[8,4,"SSSSBBBB"*2],[4,2,"SSSSBBBB"*2],[2,1,"SSSSBBBB"*2],[16,8,"SSSSSSSSBBBBBBBB"*1],[8,4,"SSSSSSSSBBBBBBBB"*1],[4,2,"SSSSSSSSBBBBBBBB"*1],[2,1,"SSSSSSSSBBBBBBBB"*1],"Done",[16,8,"S"*16],[8,4,"S"*16],[4,2,"S"*16],[2,1,"S"*16]]
    # for i in [2,3,4]:
    #     for j in range(i,0,-1):
    #         s32.append([2**j,2**(j-1),(("S"*2)+("B"*2))*4 if i==4 else ("S"*8)+("B"*8)])
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
        # print(type(i)is str,type(i),i)
        # print(i)
        if type(i)is str or i[0]>len(lst):
            # print(i)
            continue
        b=[]
        for j in range(0,len(lst),i[0]):
            b.append(lst[j:j+i[0]])
        # print("\n",b,"\n",i)
        stp=0
        # lst=[]
        for j in range(len(b)):
            # print(j)
            for k in range(0,int(len(b[j])/2)):#,i[1]):#0,,i[1]):
                mode=i[2][stp]
                # print(b[j][k],b[j][k+i[1]])
                n1,n2=b[j][k],b[j][k+i[1]]
                # print(i[1],k,k+i[1],len(b[j]),
                # print([n1,n2],mode,k,k+i[1])
                # print([n1,n2])
                if mode=="S":
                    # print(mode)
                    n1,n2=min(n1,n2),max(n1,n2)
                else:
                    # print(mode,"b")
                    n1,n2=max(n1,n2),min(n1,n2)
                b[j][k],b[j][k+i[1]]=n1,n2
                # print([n1,n2])
                stp+=1
                # lst.append(n1)
                # lst.append(n2)
        # print(b)
        lst=[]
        for k in b:
            for j in k:
                lst.append(j)
        # input(lst)
        # print(",\033[0m".join([("\033[41m"if (a%i[0]<i[1])==0 else "\033[42m")+str(a) for a,_ in enumerate(lst)])+"\033[0m",i)
    end=time.perf_counter_ns()
    # print()
    return (lst,strt,end,end-strt)
