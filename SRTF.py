
def initialize(process,total_processes):
    for index in range(int(total_processes)):
        process.append([])
        process[index].append(input("Enter process name:"))
        process[index].append(int(input("Enter arrival time:")))
        process[index].append(int(input("Enter burst time:")))

def sorting_function(process):
    process.sort(key=lambda process:process[1])




def calculate(process,total_processes):
    endtime=[]
    ready=[]
    sum=process[0][1]
    for index in range(int(total_processes)):
        #process[index].append(sum-process[index][1])
       # sum+=process[index][2]
       # process[index].append(sum-process[index][1])
       for index2 in range (index+1,int(total_processes)):
           if (sum+process[index][2])< process[index2][1] and( process[index][2]-process[index2][1]) < process[index2][2]:
               y


def print_func(process,total_processes):
    AvgTurn=0
    AvgWait=0
    print("Process name    Arrival Time    Burst Time    Waiting time    Turn Around Time")
    index=0
    for index in range(int(total_processes)):
        print(process[index][0] ,'\t\t\t\t',process[index][1],'\t\t\t\t',process[index][2],'\t\t\t\t',process[index][3],'\t\t\t\t',process[index][4])
        AvgTurn+=process[index][3]
        AvgWait+=process[index][4]
    AvgWait=AvgWait/(int)(total_processes)
    AvgTurn=AvgTurn/(int)(total_processes)

    print("average waiting time is ", AvgWait)
    print("average turnaround time is ",AvgTurn)

process=[]
total_processes=input("Enter total number of processes: ")
initialize(process,total_processes)
sorting_function(process)
calculate(process,total_processes)
print_func(process,total_processes)

