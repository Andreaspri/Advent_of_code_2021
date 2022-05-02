#include <stdio.h>
#include <malloc.h>

int main()
{
    int count=0;
    int temp1;
    int rowN=0;
    int columN=0;
    int rows[128]={0};
    int columns[8]={0};
    char code[100];
    int* leftR;
    int* rightR;
    int* leftC;
    int* rightC;
    int* seat_id = calloc(1,sizeof(int));
    FILE* file = fopen("../data.txt","r");
    for (int i = 0; i < 128; ++i)
    {
        rows[i] = i;
        if (i < 8)
            columns[i] = i;
    }
    while (!feof(file))
    {
        fgets(code,100,file);
        rightR = &rows[127];
        leftR = &rows[0];
        leftC = &columns[0];
        rightC = &columns[7];
        seat_id = realloc(seat_id,sizeof(int)*(count+1));

        for (int i = 0; i < 10; ++i)
        {
            if (code[i] == 'F')
            {
                if (*rightR-1 == *leftR || *rightR == *leftR)
                    rowN = *leftR;
                else
                    rightR = &rows[*rightR-(*rightR - *leftR) / 2-1];
            }
            else if (code[i] == 'B')
            {
                if (*leftR+1 == *rightR || *leftR == *rightR)
                    rowN = *rightR;
                else
                    leftR = &rows[(rightR - leftR) / 2+1+*leftR];
            }
            else if (code[i] == 'R')
            {
                if (*leftC+1 == *rightC || *leftC == *rightC)
                    columN = *rightC;
                else
                    leftC = &columns[(rightC - leftC) / 2+1+*leftC];
            }
            else if (code[i] == 'L')
            {
                if (*rightC-1 == *leftC || *rightC == *leftC)
                    columN = *leftC;
                else
                    rightC = &columns[*rightC-(*rightC - *leftC) / 2-1];
            }
        }
        seat_id[count] = rowN*8+columN;
        rowN = 0;
        columN = 0;
        count++;
    }
    fclose(file);


    for (int i = 0; i < count-1; ++i)
    {
        for (int j = 0; j < count-i-1; ++j)
        {
            if (seat_id[j] > seat_id[j+1])
            {
                temp1 = seat_id[j];
                seat_id[j] = seat_id[j+1];
                seat_id[j+1] = temp1;
            }
        }
    }


    printf("Part 1: %i\n",seat_id[count-1]);

    for (int i = 0; i < count-1; ++i)
    {
        if ((seat_id[i]+1) != seat_id[i+1])
        {
            printf("Part 2: %i",seat_id[i]+1);
            break;
        }
    }
    free(seat_id);


}