#include "node.cpp"
#include <limits>

using namespace std;

class Solution {
private:
    bool dfs(TreeNode* node, int min_val, int max_val) {
        if (!node)
            return true;
        if (!(min_val < node->val && max_val > node->val))
            return false;

        return (dfs(node->right, node->val, max_val) &&
                dfs(node->left, min_val, node->val));
    }

public:
    bool isValidBST(TreeNode* root) {
        int Inf = numeric_limits<float>::infinity();
        int neg_Inf = Inf*-1;

        return dfs(root, neg_Inf, Inf);
    }   
};