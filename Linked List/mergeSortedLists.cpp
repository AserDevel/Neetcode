#include <iostream>
#include <vector>
#include "node.cpp"

using namespace std;

// Sorting solution
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode* head = new ListNode();
        ListNode* res = head;
        
        while (!lists.empty()) {
            int size = lists.size();
            // Insertion sort
            for (int i = 1; i < size; i++) {
                ListNode* cur = lists[i];
                int j = i - 1;

                while (j >= 0 && cur->val < lists[j]->val) {
                    lists[j + 1] = lists[j];
                    j--;
                }
                lists[j + 1] = cur;
            }
            
            // Insert all nodes with the minimun value
            int minVal = lists[0]->val;
            int n = 0;
            while (n < size && lists[n]->val == minVal) {
                head->next = lists[n];
                head = head->next;
                lists[n] = lists[n]->next;
                n++;
            }

            // Remove empty lists
            for (int i = size - 1; i >= 0; i--)
                if (lists[i] == NULL)
                    lists.erase(lists.begin() + i);
        }

        return res->next;
    }
};


// Merge solution (optimal)
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty())
            return NULL;

        for (int i = 1; i < lists.size(); i++) 
            lists[0] = merge(lists[0], lists[i]); 
        
        return lists[0];
    }

private:
    ListNode* merge(ListNode* list1, ListNode* list2) {
        ListNode* head = new ListNode();
        ListNode* curr = head;
        while (list1 && list2) {
            if (list1->val <= list2->val) {
                curr->next = list1;
                list1 = list1->next;
            } else {
                curr->next = list2;
                list2 = list2->next;
            }
            curr = curr->next;
        }
        if (list1)
            curr->next = list1;
        else
            curr->next = list2;

        return head->next;
    }
};
