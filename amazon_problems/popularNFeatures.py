def popularNFeatures(numFeatures, topFeatures, possibleFeatures, 
                    numFeatureRequests, featureRequests):
    # WRITE YOUR CODE HERE
    #print numFeatures, topFeatures, possibleFeatures, numFeatureRequests, featureRequests
    featureDict = dict.fromkeys(possibleFeatures, 0)
    
    for request in featureRequests:
        setRequest = createFeatureSet(request)
        feature_check = checkFeatureRequest(possibleFeatures, request)
        
        if feature_check:
            for feature in feature_check:
                featureDict[feature] += 1
    
    sorted_feature_dict = sorted(featureDict.items(), key=lambda x: x[1], reverse=True)
    # print "featureDict = ", featureDict

    feture_list = getTopFeatures(topFeatures, featureDict)
    return feture_list#' '.join(feture_list)

def createFeatureSet(requestComment):
    comment = requestComment.split()
    featureSet = set()
    
    for str in comment:
        featureSet.add(str)
    
    return featureSet
    
def checkFeatureRequest(possibleFeatures, comment):#setRequest):
    #print "comment = " , comment
    features = []
    for possibleFeature in possibleFeatures:
        if possibleFeature in comment:#setRequest:
            features.append(possibleFeature)
    if features:
        return features
    else:
        return None
    
    
def getTopFeatures(topFeatures, featureDict):
    featureResult = []
    #print featureDict
    topFeature = sorted(featureDict.items(), key=lambda x: x[1], reverse=True)
    #print "topFeature = ", topFeature
    minus_result = []
    counter = topFeatures
    for i in range(len(topFeature) - 1):
        if topFeature[i][1] != topFeature[i + 1][1] and topFeature[i + 1][1] > 0:
            counter -= 1
            featureResult.append(topFeature[i][0])
        elif topFeature[i][1] > 0:
            minus_result.append(topFeature[i][0])
    minus_result.sort()
    return featureResult + minus_result[:counter]