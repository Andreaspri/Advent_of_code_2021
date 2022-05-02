//
// Created by Andreas on 29.04.2022.
//

#ifndef LLIST_LLIST_H
#define LLIST_LLIST_H

#include <stdexcept>
#include <iostream>
#include <map>


template <typename T> class LList {
private:
    bool circular{};
    bool mapped{};

    struct Node {
        T data;
        Node *next;
        Node *prev;
    };

    Node *head;
    Node *tail;
    int length;

    std::map<T, Node*> map;

public:
    explicit LList(bool circular = false, bool mapped = false);
    void append(T data);
    void insert(T data, int index);
    void removeIndex(int index);
    void remove(T data);
    void clear();
    T get(int index = 0);
    void next();
    int size();
    void print(int from=0);
    bool isCircular();
    int find(T data);
    void moveByIndex(int from, int to, int count=1);
    void moveByData(T from, T to, int count=1);
    

    class iterator {
    private:
        Node *current;
    public:
        explicit iterator(Node *node) : current(node){}
        iterator &operator++() {
            current = current->next;
            return *this;
        }
        iterator &operator--() {
            current = current->prev;
            return *this;
        }
        T &operator*() {
            return current->data;
        }
        bool operator==(const iterator &other) const {
            return current == other.current;
        }


        bool operator!=(const iterator &other) const{
                return current != other.current;
         }

    };

    LList<T>::iterator begin();
    LList<T>::iterator end();
};



template<typename T>
typename LList<T>::iterator LList<T>::begin() {
    return iterator(head);
}

template<typename T>
typename LList<T>::iterator LList<T>::end() {
    if (circular)
        throw std::logic_error("Circular list does not have an end");
    else
        return iterator(tail->next);
}








template<typename T>
LList<T>::LList(bool cir, bool map) {
    this->circular = cir;
    this->mapped = map;
    head = nullptr;
    tail = nullptr;
    length = 0;
}


template<typename T>
void LList<T>::append(T data) {
    Node *newNode = new Node;
    newNode->data = data;
    newNode->next = nullptr;
    newNode->prev = nullptr;

    if (mapped) {
        map[data] = newNode;
    }

    if (head == nullptr) {
        head = newNode;
        tail = newNode;
        if (circular) {
            head->prev = tail;
            tail->next = head;
        }
    } else {
        tail->next = newNode;
        newNode->prev = tail;
        tail = newNode;
        if (circular) {
            tail->next = head;
            head->prev = tail;
        }
    }
    length++;
}

template<typename T>
void LList<T>::insert(T data, int index) {
    if (index < 0 || index > length) {
        throw std::out_of_range("Index out of range");
    }

    Node *newNode = new Node;
    newNode->data = data;
    newNode->next = nullptr;
    newNode->prev = nullptr;

    if (mapped) {
        map[data] = newNode;
    }


    if (head == nullptr)
    {
        head = newNode;
        tail = newNode;
        if (circular) {
            head->prev = tail;
            tail->next = head;
        }
    }
    else if (index == 0) {
        newNode->next = head;
        head->prev = newNode;
        head = newNode;
        if (circular) {
            head->prev = tail;
            tail->next = head;
        }
    }
    else if (index == length) {
        tail->next = newNode;
        newNode->prev = tail;
        tail = newNode;
        if (circular) {
            tail->next = head;
            head->prev = tail;
        }
    }
    else
    {
        Node *current = head;
        for (int i = 0; i < index; i++) {
            current = current->next;
        }
        newNode->next = current;
        newNode->prev = current->prev;
        current->prev->next = newNode;
        current->prev = newNode;
    }
    length++;
}

template<typename T>
void LList<T>::removeIndex(int index) {
    if (index < 0)
        index += length;
    if (index >= length)
        index -= length;

    if (index < 0 || index >= length) {
        throw std::out_of_range("Index out of range");
    }

    if (index == 0) {
        if (head == tail && length == 1) {
            map.erase(head->data);
            delete head;
            head = nullptr;
            tail = nullptr;
        } else {
            Node *temp = head;
            head = head->next;
            if (circular) {
                temp->prev->next = temp->next;
                temp->next->prev = temp->prev;
            }
            else
                head->prev = nullptr;
            map.erase(temp->data);
            delete temp;
        }
    } else if (index == length - 1) {
        Node *temp = tail;
        tail = tail->prev;
        if (circular) {
            temp->prev->next = temp->next;
            temp->next->prev = temp->prev;
        }
        else
            tail->next = nullptr;
        map.erase(temp->data);
        delete temp;
    } else {
        Node *current = head;
        for (int i = 0; i < index; i++) {
            current = current->next;
        }
        current->prev->next = current->next;
        current->next->prev = current->prev;
        map.erase(current->data);
        delete current;
    }
    length--;
}

template<typename T>
void LList<T>::remove(T data) {
    Node *current = head;
    do {
        if (current->data == data) {
            if (current == head) {
                if (head == tail && length == 1) {
                    map.erase(head->data);
                    delete head;
                    head = nullptr;
                    tail = nullptr;
                }
                else
                {
                    head = head->next;
                    if (circular) {
                        current->prev->next = current->next;
                        current->next->prev = current->prev;
                    }
                    else
                        head->prev = nullptr;
                    map.erase(current->data);
                    delete current;
                }
            }
            else if (current == tail) {
                tail = tail->prev;
                if (circular) {
                    current->prev->next = current->next;
                    current->next->prev = current->prev;
                }
                else
                    tail->next = nullptr;
                map.erase(current->data);
                delete current;
            }
            else
            {
                current->prev->next = current->next;
                current->next->prev = current->prev;
                map.erase(current->data);
                delete current;
            }
            length--;
            return;
        }
        current = current->next;
    } while (current != nullptr && current != head);
}

template<typename T>
void LList<T>::clear() {
    while (head != nullptr && length != 0) {
        Node *temp = head;
        head = head->next;
        map.erase(temp->data);
        delete temp;
        length--;
    }
    head = nullptr;
    tail = nullptr;
}

template<typename T>
T LList<T>::get(int index) {
    if (index < 0)
        index += length;
    if (index >= length)
        index -= length;

    if (index < 0 || index >= length) {
        throw std::out_of_range("Index out of range");
    }

    Node *current = head;
    for (int i = 0; i < index; i++) {
        current = current->next;
    }
    return current->data;
}

template<typename T>
int LList<T>::size()
{
    return length;
}

template<typename T>
void LList<T>::print(int from) {
    if (length < 1)
        return;
    Node *current = head;
    for (int i = 0; i < from; i++) {
        current = current->next;
    }
    do {
        std::cout << current->data << " ";
        current = current->next;
    } while (current != head && current != nullptr);
    std::cout << std::endl;
}

template<typename T>
void LList<T>::moveByIndex(int from, int to, int count) {
    if (from < 0)
        from += length;
    if (to < 0)
        to += length;
    if (from >= length)
        from -= length;
    if (to >= length)
        to -= length;

    if (circular) {
        if (from < 0 || from >= length || to < 0 || to >= length) {
            throw std::out_of_range("Index out of range");

        }
        if ((from + count -length -1) >= to)
            return;

    } else if (from < 0 || from >= length || to < 0 || to > length || from + count > length || from + count < 0) {
        throw std::out_of_range("Index out of range");
    }


    if (from == to || count == 0 || count == length || (from + count > to && from < to)) {
        return;
    }

    Node *current = head;
    for (int i = 0; i < from; i++) {
        current = current->next;
    }
    Node *start = current;
    for (int i = 0; i < count-1; i++) {
        current = current->next;
    }
    Node *end = current;

    current = head;
    for (int i = 0; i < to; i++) {
        current = current->next;
    }
    Node *target = current;

    if (circular)
    {
        start->prev->next = end->next;
        end->next->prev = start->prev;

        end->next = target->next;
        target->next->prev = end;
        target->next = start;
        start->prev = target;

        return;

    } else {
        if (head == start) {
            head = end->next;


        } else if (tail == end) {
            tail = start->prev;
            start->prev->next = end->next;

        } else {
            start->prev->next = end->next;
            end->next->prev = start->prev;
        }

        if (head == target) {
            head = start;
            start->prev = target->prev;
            end->next = target;
            target->prev = end;

        } else if (target == nullptr) {
            tail->next = start;
            start->prev = tail;
            tail = end;
            end->next = target;
        }else if (target == tail)
        {
            start->prev = target;
            end->next = target->next;
            target->next = start;
            tail = end;
        }
        else {
            if (from > to) {
                start->prev = target->prev;
                target->prev->next = start;

                end->next = target;
                target->prev = end;
            }
            else {
                start->prev = target;
                end->next = target->next;
                target->next->prev = end;
                target->next = start;
            }
        }
    }
}

template<typename T>
bool LList<T>::isCircular() {
    return circular;
}

template<typename T>
int LList<T>::find(T data) {
    Node *current = head;
    int index = 0;
    do {
        if (current->data == data) {
            return index;
        }
        current = current->next;
        index++;
    } while (current != head && current != nullptr);
    return -1;
}

template<typename T>
void LList<T>::next() {
    if (circular)
        head = head->next;
    else
        throw std::logic_error("Cant move head of non circular list");

}


template<typename T>
void LList<T>::moveByData(T from, T to, int count) {
    if (!mapped) {
        if (from == to || count == 0 || count == length || (from + count > to && from < to))
            return;
        int fromIndex = find(from);
        int toIndex = find(to);
        moveByIndex(fromIndex, toIndex, count);
    }
    else
    {
        Node *fromNode = map[from];
        Node *toNode = map[to];
        Node * endNode = fromNode;

        for (int i = 0; i < count-1; ++i)
        {
            if (toNode == endNode)
                throw std::logic_error("Cant move to the same node or node in the middle of the range");
            endNode = endNode->next;
        }
            fromNode->prev->next = endNode->next;
            endNode->next->prev = fromNode->prev;

            fromNode->prev = toNode;
            endNode->next = toNode->next;
            toNode->next->prev = endNode;
            toNode->next = fromNode;


    }
}




#endif //LLIST_LLIST_H
