#include <stdio.h> #include <stdlib.h>

int main()

int requests[100], n, head, i; int seek_time = 0; int distance, cur_track;

printf("Enter the number of disk requests: "); scanf("%d", &n);

printf("Enter the disk requests:\n"); for(i = 0; i<n; i++)

scanf("%d", &requests[i]);

printf("Enter the initial head position: "); scanf("%d", &head);

printf("\ nSeek Sequence is:\n");

for(i = 0; i<n; i++)

cur_track = requests[i];

printf("%d -> ", cur_track);

distance = abs(cur_track - head);

seek time += distance;

head = cur_track;

printf("\n\nTotal Seek Time = %d\n", seek_time);

return 0;

Output:-

Enter the number of disk requests: 7 Enter the disk requests: 82 170 43 140 24 16 190 Enter the initial head position: 50

Seek Sequence is: 82 -> 170 -> 43 -> 140 -> 24 -> 16 -> 190 ->

Total Seek Time = 642
