#include <iostream>

#include "llist.h"



void part1(LList<int> *list)
{

    list->append(8);
    list->append(7);
    list->append(1);
    list->append(3);
    list->append(6);
    list->append(9);
    list->append(4);
    list->append(5);
    list->append(2);

    for (int i = 0; i < 100; i++) {
        int current = list->get();
        int cup1 = list->get(1);
        int cup2 = list->get(2);
        int cup3 = list->get(3);

        int destination = current;


        do {
            destination--;
            if (destination < 1)
                destination = 9;
        }while(destination == cup1 || destination == cup2 || destination == cup3);

        list->moveByData(cup1, destination, 3);

        list->next();
    }
}



long long part2(LList<int> list)
{

    list.append(8);
    list.append(7);
    list.append(1);
    list.append(3);
    list.append(6);
    list.append(9);
    list.append(4);
    list.append(5);
    list.append(2);

    for (int i = 10; i < 1000001; ++i) {
        list.append(i);
    }


    for (int i = 0; i < 10000000; i++) {
        int current = list.get();
        int cup1 = list.get(1);
        int cup2 = list.get(2);
        int cup3 = list.get(3);

        int destination = current;


        do {
            destination--;
            if (destination < 1)
                destination = 1000000;
        }while(destination == cup1 || destination == cup2 || destination == cup3);

        list.moveByData(cup1, destination, 3);

        list.next();
    }

    int index1 = list.find(1);

    long long first = list.get(index1+1);
    long long second = list.get(index1+2);

    return first * second;
}


int main() {
    LList<int> list(true, true);

    part1(&list);
    int start = list.get(1);
    std::cout << "Part 1: ";
    for (int i = 0; i < list.size()-1; i++) {
        std::cout << list.get(i+start+1);
    }
    std::cout << std::endl;

    list.clear();

    std::cout << "Part 2: " << part2(list) << std::endl;

    return 0;
}
