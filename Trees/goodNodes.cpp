#include "node.cpp"

class Solution {
private:
    int res;
    void dfs(TreeNode* node, int maxValue) {
        if (!node)
            return;

        if (node->val >= maxValue) {
            res++;
            maxValue = node->val;
        }

        dfs(node->left, maxValue);   
        dfs(node->right, maxValue);
        return;
    }

public:
    int goodNodes(TreeNode* root) {
        res = 0;
        dfs(root, root->val);
        return res;
    }
};