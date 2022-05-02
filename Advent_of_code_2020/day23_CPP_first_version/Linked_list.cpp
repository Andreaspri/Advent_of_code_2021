//
// Created by Andreas on 28.04.2022.
//

#include <iostream>
#include "Linked_list.h"






Linked_list::Linked_list(int value) {
    this->head = new Node;
    this->head->value = value;
    this->tail = this->head;
    this->head->next = this->tail;
    this->head->prev = this->tail;
    map[value] = this->head;
}



Linked_list::~Linked_list() {
    Node* current = this->head;
    Node* next;
    do {
        next = current->next;
        delete current;
        current = next;
    } while (current != this->head);
}



void Linked_list::new_node(int value) {
    Node* new_node = new Node;
    new_node->value = value;
    new_node->next = this->head;
    this->tail->next = new_node;
    new_node->prev = tail;
    this->tail = new_node;
    this->head->prev = new_node;
    map[value] = new_node;
}



Node* Linked_list::pop_nodes(int from, int count) {
    Node* from_node = map[from];

    from_node = from_node->next;

    Node* temp = from_node;
    for (int i = 0; i < count-1; i++) {
        temp = temp->next;
    }

    from_node->prev->next = temp->next;
    temp->next->prev = from_node->prev;

    from_node->prev = nullptr;
    temp->next = nullptr;

    return from_node;

}



void Linked_list::insert_nodes(int value, Node *node) {
    Node* current = map[value];

    Node* last_node = node;

    while (last_node->next != nullptr) {
        last_node = last_node->next;
    }

    last_node->next = current->next;
    current->next->prev = last_node;
    current->next = node;
    node->prev = current;


}

void Linked_list::print_list() {
    Node* current = this->head;
     do{
        std::cout << current->value << " ";
        current = current->next;
    }while (current != this->head);
    std::cout << std::endl;
}

void Linked_list::move_head() {
    this->head = this->head->next;
}










