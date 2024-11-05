#include <iostream>
#include <vector>
#include <queue>
#include "node.cpp"

using namespace std;

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        queue<TreeNode*> queue;
        
        if (root)
            queue.push(root);

        while (queue.size() > 0) {
            vector<int> level;
            for (int i = queue.size(); i > 0; i--) {
                TreeNode* curr = queue.front();
                level.push_back(curr->val);
                if (curr->left)
                    queue.push(curr->left);
                if (curr->right)
                    queue.push(curr->right);
                queue.pop();
            }
            res.push_back(level);
        }
        return res;
    }
};