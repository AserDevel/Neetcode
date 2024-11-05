#include <iostream>
#include <string.h>

using namespace std;

class PrefixTreeNode {
public:
    PrefixTreeNode* children[26];
    bool isWord;
    
    PrefixTreeNode() {
        for (int i = 0; i < 26; i++) {
            children[i] = NULL;
        }
        isWord = false;
    }
};

class PrefixTree {

private:
    PrefixTreeNode* root;

public:
    PrefixTree() {
        root = new PrefixTreeNode();
    }
    
    void insert(string word) {
        PrefixTreeNode* cursor = root;
        
        for (char c : word) {
            int curr = c - 'a';
            if (cursor->children[curr] == nullptr)
                cursor->children[curr] = new PrefixTreeNode();
            cursor = cursor->children[curr];
        }

        cursor->isWord = true;
    }
    
    bool search(string word) {
        PrefixTreeNode* cursor = root;
        
        for (char c : word) {
            int curr = c - 'a';
            if (cursor->children[curr] == nullptr)
                return false;
            cursor = cursor->children[curr];
        }

        return cursor->isWord;
    }
    
    bool startsWith(string prefix) {
        PrefixTreeNode* cursor = root;
        
        for (char c : prefix) {
            int curr = c - 'a';
            if (cursor->children[curr] == nullptr)
                return false;
            cursor = cursor->children[curr];
        }

        return true;
    }
};