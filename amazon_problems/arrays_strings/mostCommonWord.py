import re
from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = re.sub(r"[^a-zA-Z0-9]+", ' ', paragraph).strip()
        words = words.lower().split(' ')
        most_common_dict = {}
        
        # for word in words:
        #     word = word.lower().strip()
        #     if word not in banned and word:
        #         if word in most_common_dict:
        #             most_common_dict[word] = most_common_dict[word] + 1
        #         else:
        #             most_common_dict[word] = 1
        
        # most_common_dict = sorted(most_common_dict.items(), key=lambda x: x[1], reverse=True)
        return Counter(word for word in words if word not in banned).most_common(1)[0][0]
        #print most_common_dict
        #return next(iter(most_common_dict))[0]

        
        
ob = Solution()
print ob.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"])
#print ob.mostCommonWord("abcdedhbdghsk")