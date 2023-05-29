class Process:
    def __init__(self,pid,at,bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.wt = 0
        self.ct = 0
        self.tat = 0

def getAverageCompilationTime(lt,tq):
    clt = []
    ct = 0
    for i in lt:
        clt.append(i.bt)
    index = 0
    while clt != [0 for i in range(len(lt))]:
        if clt[index] <= tq:
            ct += clt[index]
            clt[index] = 0
            lt[index].ct = ct
            index = 0
        elif clt[index] > tq:
            ct += tq
            clt[index] -= tq
        if index == len(lt)-1:
            index = 0
        else:
            index+=1
    avgct = 0
    for i in lt:
        avgct += ct
    return avgct/len(lt)

def getAverageTurnAroundTime(lt,tq):
    avgtat = 0
    for i in lt:
        i.tat = i.ct-i.bt
    for i in lt:
        avgtat+=i.tat
    return avgtat/len(lt)
def getAverageWaitingTime(lt,tq):
    wt = 0
    for i in range(len(lt)):
        if i==0:
            lt[i].wt =0
        elif lt[i].bt<tq:
            wt += lt[i-1].bt - tq
            lt[i].wt = wt
        else:
            wt += tq
            lt[i].wt = wt
    avgwt = 0    
    for i in lt:
        avgwt += i.wt
    return avgwt/len(lt)


if __name__ == "__main__":
    n = int(input("enter the Number of Processes : "))
    lt = [None for i in range(n)]
    for i in range(n):
        pid = input("enter Process ID : ")
        at = int(input("enter Arrival Time"))
        bt = int(input("enter Burst Time : "))
        lt[i] = Process(pid,at,bt)
    tq = int(input("enter Time Quantum : "))
    avgct = getAverageCompilationTime(lt,tq)
    avgwt = getAverageWaitingTime(lt,tq)
    avgtat = getAverageTurnAroundTime(lt,tq)
    print("Process ID | Arrival Time | Burst Time | Compilation Time | Waiting Time | Turn Around Time")
    for i in lt:
        print("{} | {} | {} | {} | {} | {} ".format(i.pid,i.at,i.bt,i.ct,i.wt,i.tat))

    