#include "node.cpp"

class Solution {
public:
    bool hasCycle(ListNode* head) {
        int count = 0;
        while (head && count < 1000) {
            if (!head->next) 
                return false;
            head = head->next;
            count++;
        }
        return true;
    }
};

class Solution {
public:
    bool hasCycle(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
            if (fast == slow)
                return true;
        }
        return false;
    }
};