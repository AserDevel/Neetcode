#include <node.cpp>
#include <bits/stdc++.h>

class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int res = 0;
        dfs(root, res);
        return res;
    }

private:
    int dfs(TreeNode* root, int& res) {
        if (!root)
            return 0;
        int left = dfs(root->left, res);
        int right = dfs(root->right, res);
        res = std::max(res, left + right);
        return 1 + std::max(left, right);
    }
};