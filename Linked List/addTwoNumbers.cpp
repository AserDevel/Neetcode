#include <iostream>
#include <string>
#include "node.cpp"

using namespace std;

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        string n1, n2;
        while (l1) {
            n1 = to_string(l1->val) + n1;
            l1 = l1->next;
        }
        while (l2) {
            n2 = to_string(l2->val) + n2;
            l2 = l2->next;
        }
        string sum = to_string(stoi(n1) + stoi(n2));

        ListNode* dummy = new ListNode(0);
        ListNode* head = dummy;
        for (int i = sum.length(); i > 0; i--) {
            int v = sum.at(i - 1) - '0';
            dummy->next = new ListNode(v);
            dummy = dummy->next;
        }

        return head->next;
    }
};