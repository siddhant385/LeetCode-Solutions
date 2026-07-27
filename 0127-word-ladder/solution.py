class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #convert wordlist to a set and add end word to it
        wordSet = set(wordList)
        # define a queue as we will perform bfs
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        q = deque([(beginWord,1)])
        letterset=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        # now we will perform loop:
        while q:
            # we will remove word from q
            word,level = q.popleft()
            # we will check every combination of the word 1st word 2nd word 3rd word nth word
            n = len(word)
            ans = ""
            for i in range(n):
                for char in letterset:
                    lst = list(word)
                    lst[i] = char
                    ans = "".join(lst)
                    # if word exists in set add that word to queue or if we got the endWord return it
                    if ans in wordSet:
                        if ans == endWord:
                            return level+1
                        q.append((ans,level+1))
                        wordSet.remove(ans)
        return 0




           
        
        