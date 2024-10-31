#include <node.cpp>

class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (isSameTree(root, subRoot))
            return true;
        if (root)
            return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
        return false;
    }

private:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q)
            return true;
        if (p && q && p->val == q->val)
            return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        return false;
    }
};