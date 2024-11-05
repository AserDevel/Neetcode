#include <iostream>
#include <vector>
#include <queue>
#include "node.cpp"

using namespace std;

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if (!root) return res;

        queue<TreeNode*> queue;
        queue.push(root);

        while (!queue.empty()) {
            res.push_back(queue.back()->val);
            for (int i = queue.size(); i > 0; i--) {
                TreeNode* curr = queue.front();
                queue.pop();
                if (curr->left)
                    queue.push(curr->left);
                if (curr->right)
                    queue.push(curr->right);
            }
        }
        return res;
    }
};