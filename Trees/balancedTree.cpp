#include <node.cpp>
#include <math.h>
#include <bits/stdc++.h>

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        bool res = true;
        dfs(root, res);
        return res;
    }

private:
    int dfs(TreeNode* root, bool& res) {
        if (!root || !res)
            return 0;
        int l = dfs(root->left, res), r = dfs(root->right, res);
        int diff = abs(l - r);
        if (diff > 1)
            res = false;
        return std::max(l, r) + 1;
    }
};