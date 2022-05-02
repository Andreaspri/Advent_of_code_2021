#include <iostream>
# include "Linked_list.h"





Node* part1()
{
    auto* list = new Linked_list(8);
    list->new_node(7);
    list->new_node(1);
    list->new_node(3);
    list->new_node(6);
    list->new_node(9);
    list->new_node(4);
    list->new_node(5);
    list->new_node(2);





    for (int i = 0; i < 100; i++) {

        Node* move_nodes = list->pop_nodes(list->head->value,3);
        int *current_values = new int[3];
        int count = 0;

        Node* current_node = move_nodes;
        while (current_node != nullptr) {
            current_values[count] = current_node->value;
            current_node = current_node->next;
            count++;
        }
        int destination = list->head->value - 1;
        while (true)
        {
            if (current_values[0] == destination || current_values[1] == destination || current_values[2] == destination)
                destination--;
            else if (destination < 1)
                destination = 9;
            else
                break;
        }
        list->insert_nodes(destination, move_nodes);
        list->move_head();

    }

    Node* current_node = list->map[1];

    return current_node->next;
}


long long part2()
{
    auto* list = new Linked_list(8);
    list->new_node(7);
    list->new_node(1);
    list->new_node(3);
    list->new_node(6);
    list->new_node(9);
    list->new_node(4);
    list->new_node(5);
    list->new_node(2);



    for (int i = 10; i < 1000001; i++) {
        list->new_node(i);
    }


    for (int i = 0; i < 10000000; i++) {

        Node* move_nodes = list->pop_nodes(list->head->value,3);
        int *current_values = new int[3];
        int count = 0;

        Node* current_node = move_nodes;
        while (current_node != nullptr) {
            current_values[count] = current_node->value;
            current_node = current_node->next;
            count++;
        }
        int destination = list->head->value - 1;
        while (true)
        {
            if (current_values[0] == destination || current_values[1] == destination || current_values[2] == destination)
                destination--;
            else if (destination < 1)
                destination = 1000000;
            else
                break;
        }
        list->insert_nodes(destination, move_nodes);
        list->move_head();

    }

    Node* current_node = list->map[1];

    long long first_value = current_node->next->value;
    long long second_value = current_node->next->next->value;

    return first_value * second_value;
}



int main() {

    Node * start = part1();
    printf("Part 1: ");
    for (int i = 0; i < 8; i++) {
        printf("%d", start->value);
        start = start->next;
    }
    printf("\n");
    printf("Part 2: %llu\n", part2());

    return 0;
}
