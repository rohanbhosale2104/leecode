class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq={}
        #frequency of each word
        for word in words:
            freq[word]=freq.get(word,0)+1
        # sorts words by frequency and alphabetically 
        sorted_words=sorted(
            freq.keys(),
            key=lambda word:(-freq[word],word)
        )
        #return 1st k words
        return sorted_words[:k]


        