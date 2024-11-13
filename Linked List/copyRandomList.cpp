#include <iostream>
#include <vector>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};


class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return head;
        
        Node* new_head = new Node(head->val);
        vector<Node*> nodes = {head};
        vector<Node*> new_nodes = {new_head};

        while (head->next) {
            head = head->next;
            new_head->next = new Node(head->val);
            new_nodes.push_back(new_head->next);
            nodes.push_back(head);
            new_head = new_head->next;
        }

        for (int i = 0; i < nodes.size(); i++) {
            int j = 0;
            while (nodes[i]->random != nodes[j])
                j++;
            new_nodes[i]->random = (j < nodes.size()) ? new_nodes[j] : NULL;
        }

        return new_nodes[0];
    }
};