#include <iostream>
#include <queue>
#include <unordered_map>

using namespace std;

class LRUCache {
private:
    int cap;
    unordered_map<int, pair<int, int>> cache;
    queue<int> used;

public:
    LRUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        if (cache[key].first < 1) 
            return -1;
        cache[key].first += 1;
        used.push(key);
        return cache[key].second;
    }
    
    void put(int key, int value) {
        if (cache[key].first == 0)
            cap--;

        cache[key].first += 1;
        cache[key].second = value;
        used.push(key);

        while (cap < 0) {
            int cur_key = used.front();
            used.pop();
            cache[cur_key].first -= 1;
            if (cache[cur_key].first == 0) {
                cache.erase(cur_key);
                cap++;
            }                
        } 
    }
};