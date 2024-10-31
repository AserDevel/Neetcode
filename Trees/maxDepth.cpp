#include <node.cpp>

class Solution {
public:
    int maxDepth(TreeNode* root) {
        int res = 0;
        if (root) {
            int l = maxDepth(root->left), r = maxDepth(root->right);
            if (l > r)
                res = l + 1;
            else
                res = r + 1;
        }
        return res;
    }
};