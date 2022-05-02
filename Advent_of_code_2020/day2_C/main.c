#include <stdio.h>
#include <malloc.h>
#include <mem.h>

int main() {

    int start_array[1][2] = {0};
    int stop_array[1][2] = {0};
    int start = 0 ;
    int stop = 0;
    char letter;
    int count = 0;
    int temp_count = 0;
    int valid_passwords = 0;
    char** arr = malloc(sizeof(char*));


    // Del 2 variabler vv

    char password[100] = {0};
    int valid_passwords_part_2 = 0;
    int first = 0;
    int last = 0;

    // Del 2 variabler ^^


    FILE *file = fopen("../data.txt", "r");
    if (file == NULL)
        printf("Failed to open file");


    while (!feof(file))
    {
        arr = realloc(arr,sizeof(char*) * (count+1));
        arr[count] = calloc(100,sizeof(char));
        fgets(arr[count],100,file);
        count++;
    }
    for (int i = 0; i < count; ++i)
    {
        if (arr[i][1] == '-')
        {
            start_array[0][1] = arr[i][0] - '0';
            if (arr[i][3] == ' ')
            {
                stop_array[0][1] = arr[i][2] - '0';
                letter = arr[i][4];
            } else
            {
                stop_array[0][0] = arr[i][2] - '0';
                stop_array[0][1] = arr[i][3] - '0';
                letter = arr[i][5];
            }
        }
        else
        {
            start_array[0][0] = arr[i][0] - '0';
            start_array[0][1] = arr[i][1] - '0';
            stop_array[0][0] = arr[i][3] - '0';
            stop_array[0][1] = arr[i][4] - '0';
            letter = arr[i][6];
        }
        temp_count = 0;
        start = 0;
        stop = 0;
        for (int j = 0 ; j < sizeof(start_array[0])/sizeof(int) ; ++j)
        {
            start = (10*start + start_array[0][j]);
            stop = (10*stop + stop_array[0][j]);
        }
        for (int j = 0; j < (strlen(arr[i])-1); ++j)
        {
            if (letter == arr[i][j])
                temp_count++;
        }
        if (start <= temp_count-1 && temp_count-1 <= stop)
            valid_passwords++;
        memset(start_array, 0, sizeof(start_array));
        memset(stop_array, 0, sizeof(stop_array));


        // Del 2

        if (start >= 10)
        {
            if (arr[i][start+8] == letter)
                first = 1;
            if (arr[i][stop+8] == letter)
                last = 1;
        }
        if (start < 10 && stop >= 10)
        {
            if (arr[i][start+7] == letter)
                first = 1;
            if (arr[i][stop+7] == letter)
                last = 1;
        }
        if (start < 10 && stop < 10)
        {
            if (arr[i][start+6] == letter)
                first = 1;
            if (arr[i][stop+6] == letter)
                last = 1;
        }
        if (first == 1 && last != 1)
            valid_passwords_part_2++;
        else if (first != 1 && last == 1)
            valid_passwords_part_2++;
        first = 0;
        last = 0;
        memset(password,0,sizeof(password));
    }


    printf("Part 1: %i\n",valid_passwords);

    printf("Part 2: %i",valid_passwords_part_2);



}
