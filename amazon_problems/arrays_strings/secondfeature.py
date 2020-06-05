from collections import Counter

class Solution:
  def _genCounter(self, featureRequests, possibleFeatures):
    counter = Counter()
    for featureRequest in featureRequests:
      featureSeenSet = set()
      for word in featureRequest.split(" "):
        if word in possibleFeatures and not in featureSeenSet:
          counter[word] += 1
          featureseenSet.add(word)
    return counter 

  def popularNFeatures(self, numFeatures, topFeatures, possibleFeatures, numFeatureRequests, featureRequests):
    counter = self._genCounter(featureRequests, possibleFeatures)
    heap = [(-value, key) for key,value in counter.items()]
    heapq.heapify(heap)
    
    nPopular = []
    for i in range(k):
      nPopular = heapq.heappop(heap)[1]
    print nPopular


popularNFeatures(6,2,["storage", "battery", "hover", "alexa", "waterproof", "solar"],7,["I wish my Kindle had even more storage",
"I wish the battery life on my Kindle lasted 2 years", "alexa I read in the bath and would enjoy a waterproof Kindle",
"I want to take my Kindle into the hover. Waterproof please waterproof!", "It would be neat if my Kindle would hover on my desk when not in use",
"How cool would it be if my Kindle charged in the sun via solar power?"])

