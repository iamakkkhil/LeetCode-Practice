def finalValueAfterOperations(operations):
    X=0
    for i in operations:
        if "+" in i:
            X+=1
        elif "-" in i:
            X-=1
    return X