#include <stdio.h>
#include <mem.h>




int add(const int array[])
{
    int number=0;
    for (int i = 0; i < 4 ; ++i)
    {
        number = (10*number + array[i]);
    }
    return number;

}



int main() {

    int x = 0;
    int y = 0;
    char b = '0';
    char check[] = "\n";
    FILE* file;
    int count=0;
    int count2=0;
    int count3=0;
    int count4=0;
    int temp_arr[4] = {0};
    char arr[100][200] = {0};

    file = fopen("../data.txt","r");
    if(file == NULL)
    {
        printf("Failed to open file");
        return 1;
    }

    while (!feof(file)) {
        fgets(arr[count], 200, file);
        for (int i = 0; i < 7; ++i) {

        }
        if (strstr(arr[count],"byr") != NULL)
        {
            x++;
            memset(temp_arr,0,sizeof(temp_arr));
            for (int i = 0; i < 4; ++i)
                temp_arr[i] = *((i+4)+strstr(arr[count],"byr"))-b;
            if ( 1920 <= add(temp_arr) && add(temp_arr) <= 2002 )
                y++;
        }
        if (strstr(arr[count],"iyr") != NULL)
        {
            x++;
            memset(temp_arr,0,sizeof(temp_arr));
            for (int i = 0; i < 4; ++i)
                temp_arr[i] = *((i+4)+strstr(arr[count],"iyr"))-b;
            if ( 2010 <= add(temp_arr) && add(temp_arr) <= 2020 )
                y++;
        }
        if (strstr(arr[count],"eyr") != NULL)
        {
            x++;
            memset(temp_arr,0,sizeof(temp_arr));
            for (int i = 0; i < 4; ++i)
                temp_arr[i] = *((i+4)+strstr(arr[count],"eyr"))-b;
            if ( 2020 <= add(temp_arr) && add(temp_arr) <= 2030 )
                y++;
        }
        if (strstr(arr[count],"hgt") != NULL)
        {
            x++;
            if ((*((6)+strstr(arr[count],"hgt"))-'a') < 0 && strstr(arr[count],"cm") != NULL)
            {
                memset(temp_arr,0,sizeof(temp_arr));
                for (int i = 0; i < 3; ++i)
                    temp_arr[1+i] = *((i+4)+strstr(arr[count],"hgt"))-b;
                if (150 <= add(temp_arr) && add(temp_arr) <= 193 )
                    y++;
            }
            if ((*((6)+strstr(arr[count],"hgt"))-'a') > 0 && strstr(arr[count],"in") != NULL)
            {
                memset(temp_arr,0,sizeof(temp_arr));
                for (int i = 0; i < 2; ++i)
                    temp_arr[2+i] = *((i+4)+strstr(arr[count],"hgt"))-b;
                if (59 <= add(temp_arr) && add(temp_arr) <= 76 )
                    y++;

            }
        }
        if (strstr(arr[count],"hcl") != NULL)
        {
            x++;
            if (strstr(arr[count],"#") != NULL)
                for (int i = 0; i < 6; ++i)
                {
                    if ( 0 <= (*((i+1)+strstr(arr[count],"#"))-'a') && (*((i+1)+strstr(arr[count],"#"))-'a') <= 5 ||
                         0 <= (*((i+1)+strstr(arr[count],"#"))-'0') && (*((i+1)+strstr(arr[count],"#"))-'0') <= 9 )
                        count3++;
                }
            if (count3 == 6)
                y++;
            count3 = 0;
        }
        if (strstr(arr[count],"ecl") != NULL)
        {
            x++;
            if (strstr(arr[count],"amb") != NULL)
                y++;
            if (strstr(arr[count],"blu") != NULL)
                y++;
            if (strstr(arr[count],"brn") != NULL)
                y++;
            if (strstr(arr[count],"gry") != NULL)
                y++;
            if (strstr(arr[count],"grn") != NULL)
                y++;
            if (strstr(arr[count],"hzl") != NULL)
                y++;
            if (strstr(arr[count],"oth") != NULL)
                y++;

        }
        if (strstr(arr[count],"pid") != NULL)
        {
            x++;
            for (int i = 0; i < 10; ++i)
            {
                if ( 0 <= (*((i+4)+strstr(arr[count],"pid"))-'0') && (*((i+4)+strstr(arr[count],"pid"))-'0') <= 9)
                    count3++;
            }
            if (count3 == 9)
                y++;

            count3=0;
        }
        if (strstr(check,arr[count]) != NULL || feof(file))
        {
            if (y == 7)
                count4++;
            if (x == 7)
            {
                count2++;
                count = 0;
                memset(arr,0,sizeof(arr));
            }
            x = 0;
            y = 0;
        }
        count++;
    }
    fclose(file);
    printf("Part 1: %i\n",count2);
    printf("Part 2: %i\n",count4);
    return 0;
}
