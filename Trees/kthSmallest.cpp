#include <iostream>
#include <vector>
#include "node.cpp"

using namespace std;

class Solution {
private:
    int res;

    int dfs(TreeNode* node, int k, int rank) {
        if (!node)
            return 0;
        
        rank += dfs(node->left, k, 0) + 1;
        if (rank == k)
            res = node->val;
        else if (node->right)
            rank = dfs(node->right, k, rank);
    
        return rank; 
    }

public:
    int kthSmallest(TreeNode* root, int k) {
        res = 0;
        dfs(root, k, 0);
        return res;
    }
};
