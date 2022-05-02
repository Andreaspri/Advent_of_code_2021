#include <stdio.h>
#include <malloc.h>


int main() {
    FILE* file;
    int max = 0;
    int multiply=1;
    int threes=0;
    int count=0;
    int count2=0;
    int x=0;
    int pairs[5][2] = {{1,1},{3,1},{5,1},{7,1},{1,2}};

    char** hill = calloc(1,sizeof(char*));
    file = fopen("../data.txt","r");
    if (file == NULL)
    {
        printf("Failed to open file");
        return 1;
    }
    while(!feof(file))
    {
        hill = realloc(hill,sizeof(char*) * (count+1));
        hill[count] = calloc(33,sizeof(char));
        fgets(hill[count],33,file);
        hill[count][31] = 0;
        count++;
    }
    fclose(file);
    for (int k = 0; k < 5 ; ++k) {
        for (int i = 0; i < count ; ++i)
        {
            if (count2 % pairs[k][1] == 0)
            {
                if (hill[i][x] == '#')
                    threes++;
                if (x + pairs[k][0] > 30)
                    x -= 31;
                x+=pairs[k][0];
            }
            count2++;
        }
        multiply *= threes;
        if (threes > max)
            max = threes;
        threes = 0;
        x=0;
    }
    printf("Part 1: %i\n", max);
    printf("Part 2: %i\n",multiply);
    return 0;
}
