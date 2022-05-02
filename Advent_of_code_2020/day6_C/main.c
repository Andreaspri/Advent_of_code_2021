#include <stdio.h>
#include <mem.h>





int main() {
    int temp;
    int count1 = 0;
    int count2 = 0;
    int linecount = 0;
    int Nchars[26]={0};
    char line[50]={0};
    FILE *file = fopen("../data.txt", "r");
    while (!feof(file))
    {
        memset(line, 0, sizeof(line));
        fgets(line, 100, file);
        if (line[0] == '\n' || feof(file))
        {
            if (line[0] != '\n')
            {
                linecount++;
                for (int i = 0; i < strlen(line); ++i)
                {
                    temp = line[i] - 'a';
                    Nchars[temp]++;
                }}
            for (int i = 0; i < 26; ++i)
            {
                if (Nchars[i] != 0)
                    count1++;
                if (Nchars[i] == linecount)
                    count2++;
            }
            linecount=0;
            memset(Nchars, 0, sizeof(Nchars));
            continue;
        }
        linecount++;
        for (int i = 0; i < strlen(line); ++i)
        {
            temp = line[i] - 'a';
            Nchars[temp]++;
        }}
    fclose(file);
    printf("Part 1: %i\n",count1);
    printf("Part 2: %i\n",count2);
}
