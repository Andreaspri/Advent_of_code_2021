#include <stdio.h>
#include <malloc.h>


int part1(const int *array, int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; ++j)
        {
                if (array[i] + array[j] == 2020 && i != j)
                {
                    return array[i] * array[j];
                }
        }
    }
}


int part2(const int *array, int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; ++j)
        {
            for (int k = 0; k < size ; ++k) {
                if (array[i] + array[j] + array[k] == 2020 && i != j && i != k && j != k)
                {
                    return array[i] * array[j] * array[k];

                }
            }
        }
    }

}


int main() {

    int size = 0;
    FILE *file;
    int *array;
    file = fopen("../data.txt", "r");
    if (file == NULL)
    {
        printf("Failed to open file");
        return 1;
    }


    array = malloc(sizeof(int));

    while (!feof(file))
    {
        array = realloc(array,sizeof(int)*(1+size));
        fscanf(file, "%i", &array[size]);
        size++;
    }
    fclose(file);

    printf("Part 1: %i\n", part1(array,size));
    printf("Part 2: %i\n", part2(array,size));



    return 0;
}
