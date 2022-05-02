//
// Created by Andreas on 28.04.2022.
//

#ifndef DAY23_LINKED_LIST_H
#define DAY23_LINKED_LIST_H

#include "Node.h"
#include <map>

class Linked_list {

public:
    std::map<int, Node*> map;
    Node* head;
    Node* tail;

    explicit Linked_list(int value);

    ~Linked_list();

    Node* pop_nodes(int from, int count);

    void insert_nodes(int value, Node* node);

    void new_node(int value);

    void move_head();

    void print_list();



};


#endif //DAY23_LINKED_LIST_H
