#include <stdio.h>
int n, tq, time = 0;
int queue[100] = {0}, front = 0, rear = 0, a[100];
int i, j;
int gannt_chart_count = 0;

void sort();
void RoundRobin();
int select(int t);
void push(int q);
int pop();

struct data
{
    int arrival_time, service_time, burst_time, wt, tat, completion_time, process_id;
} t;

struct ganntChart
{
    int startTime;
    int ProcessId;
    int endTime;
} g[100];

void sort(struct data a[])
{
    int i, j;
    // Bubble Sort to sort the processes based on their ArrivalTime
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            if (a[j].arrival_time > a[j + 1].arrival_time)
            {
                t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
        }
    }
}

int select(int j)
{
    if (time == 0)
    {
        return j;
    }
    else
    {
        j = pop();
        return j;
    }
}

int pop()
{
    int x;
    x = queue[front++];
    return x;
}

void push(int q)
{
    queue[rear++] = q;
}

void RoundRobin(struct data a[])
{
    // Here, i is
    // j indicates the current process to be executed
    // x helps us to keep a track of the number of processes remaining to get executed
    int i = 1, j = 0, x;
    x = n;

    int start_time = 0;
    int end_time = 0;

    while (x != 0)
    {
        // Selecting the process
        j = select(j);

        // Checking if the selected process BurstTime is smaller than TimeQuantum
        if (a[j].burst_time <= tq && a[j].burst_time > 0)
        {
            // Incrementing the System Time
            g[gannt_chart_count].ProcessId = a[j].process_id;
            g[gannt_chart_count].startTime = time;
            time = time + a[j].burst_time;
            g[gannt_chart_count].endTime = time;
            gannt_chart_count++;
            // If TimeQuantum >= BurstTime then after process execution burst time = 0
            a[j].burst_time = 0;
        }
        // Checking is the selected process's BurstTime is greater than TimeQuantum
        else if (a[j].burst_time > 0)
        {
            // Subracting the TimeQuantum from BurstTime as process has been executed for TimeQuantum time.
            a[j].burst_time = a[j].burst_time - tq;
            // Incrementing the System Time
            g[gannt_chart_count].ProcessId = a[j].process_id;
            g[gannt_chart_count].startTime = time;
            time = time + tq;
            g[gannt_chart_count].endTime = time;
            gannt_chart_count++;
        }

        // Pushing the processes in readyQueue whose arrival time is smaller or equal than current system time
        while (a[i].arrival_time <= time && i < n)
        {
            // Push the process 'i' in readyQueue and increment 'i'.
            push(i);
            i++;
        }

        // If the process has completed execution
        if (a[j].burst_time == 0)
        {
            // decrement x and calculate wt and tat.
            x--;
            a[j].completion_time = time;
            a[j].wt = time - a[j].arrival_time - a[j].service_time;
            a[j].tat = a[j].wt + a[j].service_time;
        }
        // if process has not completed execution then again push it into readyQueue.
        else
        {
            push(j);
        }

        // ReadyQueue Status
        for (int k = front; k < rear; k++)
        {
            printf("%d\t", a[queue[k]].process_id);
        }
        printf("\n");
    }
}

int main()
{
    int i;
    float avg_WT = 0, avg_TAT = 0;

    // Number of Processes
    printf("Enter the no of processes :   ");
    scanf("%d", &n);

    // Making array of data to store processes
    struct data P[n];

    // Taking Input from user for ArrivalTime and BurstTime
    for (i = 0; i < n; i++)
    {
        printf("Enter the process Process %d's arival time and burst time :  ", i + 1);
        scanf("%d%d", &P[i].arrival_time, &P[i].burst_time);
        P[i].process_id = i + 1;
        P[i].service_time = P[i].burst_time;
    }

    // Time Quantum
    printf("Enter time_quantum :  ");
    scanf("%d", &tq);
    printf("\nReady Queue Status: \n");

    // Sorting the Processes based on ArrivalTime
    sort(P);

    // Applying RoundRobin on Sorted Processes
    RoundRobin(P);

    // Gannt Chart
    printf("Gannt Chart:  \n");
    printf("ProcessID  StartTime  EndTime \n");
    for (int i = 0; i < gannt_chart_count; i++)
    {
        printf("%d \t\t %d \t\t %d \n", g[i].ProcessId, g[i].startTime, g[i].endTime);
    }

    // Printing the data
    printf("\n     ProcessID     ArrivalTime     BurstTime     WaitingTime     TurnAroundTime     Completion");
    for (i = 0; i < n; i++)
    {
        printf("\n|\tp[%d]\t|\t%d\t|\t%d \t|\t%d\t|\t%d\t|\t%d\t|", P[i].process_id, P[i].arrival_time, P[i].service_time, P[i].wt, P[i].tat, P[i].completion_time);
        avg_WT += P[i].wt;
        avg_TAT += P[i].tat;
    }
    printf("\n Average waiting_time:%f \n Average turn_around_time :%f", avg_WT / n, avg_TAT / n);

    return 0;
}

/*
OUTPUT:

Enter the no of processes :   5
Enter the process Process 1's arival time and burst time :  0 8
Enter the process Process 2's arival time and burst time :  5 2
Enter the process Process 3's arival time and burst time :  1 7
Enter the process Process 4's arival time and burst time :  6 3
Enter the process Process 5's arival time and burst time :  8 5
Enter time_quantum :  3

Ready Queue Status:
3   1
1   2   4   3
2   4   3   5   1
4   3   5   1
3   5   1
5   1   3
1   3   5
3   5
5

Gannt Chart:
ProcessID  StartTime  EndTime
1        0       3
3        3       6
1        6       9
2        9       11
4        11          14
3        14          17
5        17          20
1        20          22
3        22          23
5        23          25

     ProcessID     ArrivalTime     BurstTime     WaitingTime     TurnAroundTime     Completion
|   p[1]    |   0   |   8   |   14  |   22  |   22  |
|   p[3]    |   1   |   7   |   15  |   22  |   23  |
|   p[2]    |   5   |   2   |   4   |   6   |   11  |
|   p[4]    |   6   |   3   |   5   |   8   |   14  |
|   p[5]    |   8   |   5   |   12  |   17  |   25  |
 Average waiting_time:10.000000
 Average turn_around_time :15.000000
*/
