def createSet(req):
	a = req.split()
	s = set()
	for string in a:
		s.add(string.lower())

	return s

def checkFeature(possibleFeatures, setRequest):
	for feature in possibleFeatures:
		if feature in setRequest:
			return feature
	return None

def topFeat(topFeatures, featuredic):
	print featuredic
	featureResult = []
	top = sorted(featuredic.items(), key=lambda x: x[1], reverse=True)
	minusResult = []
	print topFeatures
	counter = topFeatures
	for i in range(len(top) - 1):
		if top[i][1] != top[i + 1][1] and top[i + 1][1] > 0:
			counter -= 1
			featureResult.append(top[i][0])
		elif top[i][1] > 0:
			minusResult.append(top[i][0])
	minusResult.sort()
	return featureResult + minusResult[:counter]

def popularNFeatures(numFeatures, topFeatures, possibleFeatures, numFeatureRequests, featureRequests):
	print "insides"
	featuredic = dict.fromkeys(possibleFeatures, 0)

	for req in featureRequests:
		setRequest = createSet(req)
		feature = checkFeature(possibleFeatures, setRequest)
		if feature != None:
			featuredic[feature] += 1

	print topFeat(topFeatures, featuredic)


popularNFeatures(6,2,["storage", "battery", "hover", "alexa", "waterproof", "solar"],7,["I wish my Kindle had even more storage",
"I wish the battery life on my Kindle lasted 2 years", "I read in the waterproof bath and would enjoy a Waterproof Kindle",
"I want to take my Kindle into the hover. Waterproof please waterproof!", "It would be neat if my Kindle would hover on my desk when not in use",
"How cool would it be if my Kindle charged in the sun via solar power?"])



