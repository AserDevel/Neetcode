#include <iostream>
#include <string>
#include <vector>

using namespace std;

class TrieNode {
public:
    vector<TrieNode*> children;
    bool word;

    TrieNode() : children(26, nullptr), word(false) {}
};

class WordDictionary {
public:
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* cursor = root;
        
        for (char c : word) {
            int curr = c - 'a';
            if (cursor->children[curr] == nullptr)
                cursor->children[curr] = new TrieNode();
            cursor = cursor->children[curr];
        }

        cursor->word = true;
    }
    
    bool search(string word) {
        return dfs(word, 0, root);
    }

private:
    TrieNode* root;

    bool dfs(string word, int j, TrieNode* node) {
        TrieNode* cursor = node;

        for (int i = j; i < word.size(); i++) {
            int curr = word[i] - 'a';
            if (word[i] == '.') {
                for (TrieNode* child : cursor->children) {
                    if (child && dfs(word, i + 1, child))
                        return true;
                }
                return false;
            } else {
                if (cursor->children[curr] == nullptr)
                    return false;
                cursor = cursor->children[curr];
            }
        }
        return cursor->word;
    }
};