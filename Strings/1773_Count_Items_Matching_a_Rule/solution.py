 def countMatches(items, ruleKey, ruleValue):
    index_to_check = 0
    if ruleKey == "type":
        index_to_check = 0
    elif ruleKey == "color":
        index_to_check = 1
    elif ruleKey == "name":
        index_to_check = 2
    
    count = 0
    for item in items:
        if item[index_to_check] == ruleValue:
            count+=1
            
    return count


items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

print(countMatches(items, ruleKey, ruleValue))