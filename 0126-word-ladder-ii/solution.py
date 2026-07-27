from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # Step 1: BFS to build the graph (Adjacency List)
        # graph[word] me us word ke saare 'parents' store honge
        graph = defaultdict(list)
        
        # Hum queue me lists ke bajaye sirf set of words rakhenge current level ke liye
        current_layer = set([beginWord])
        wordSet.discard(beginWord)
        
        found = False
        alpha = 'abcdefghijklmnopqrstuvwxyz'

        while current_layer and not found:
            # Agle level me jaane se pehle, current layer ke saare words Set se hata do
            # Taaki same level ke words ek dusre ko cross na karein
            for word in current_layer:
                wordSet.discard(word)
            
            next_layer = set()
            
            for word in current_layer:
                word_list = list(word)
                for i in range(len(word)):
                    temp = word_list[i]
                    for char in alpha:
                        word_list[i] = char
                        newWord = "".join(word_list)
                        
                        if newWord in wordSet:
                            next_layer.add(newWord)
                            # Graph me record karo ki newWord kahan se aaya (uska parent 'word' hai)
                            graph[newWord].append(word)
                            
                            if newWord == endWord:
                                found = True
                    # Backtrack the character
                    word_list[i] = temp
            
            # Move to the next level
            current_layer = next_layer
        
        # Step 2: DFS to build paths starting from endWord back to beginWord
        ans = []
        
        def dfs(node, path):
            # Base case: agar hum wapas beginWord tak pohoch gaye
            if node == beginWord:
                # Path ulta hai (endWord -> beginWord), isliye reverse karke append karenge
                ans.append(path[::-1])
                return
            
            # Us node ke saare parents par DFS lagao
            for parent in graph[node]:
                path.append(parent)
                dfs(parent, path)
                path.pop() # Backtracking step
        
        # Agar endWord mila hi nahi BFS me, toh DFS chalane ka fayda nahi
        if found:
            dfs(endWord, [endWord])
            
        return ans