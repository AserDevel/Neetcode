#include <node.cpp>

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root) 
            return root;
        if (root->right)
            invertTree(root->right);
        if (root->left)
            invertTree(root->left);
        
        TreeNode* tmp = root->left;
        root->left = root->right;
        root->right = tmp; 

        return root; 
    }
};