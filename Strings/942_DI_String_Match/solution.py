def diStringMatch(s: str):
    i_perm = 0
    d_perm = len(s)
    output = []

    for i in range(len(s)):
        if s[i] == "I":
            output.append(i_perm)
            i_perm+=1
            
        elif s[i] == "D":
            output.append(d_perm)
            d_perm-=1
    
    if s[-1] == "I":
        output.append(d_perm)
            
    elif s[-1] == "D":
        output.append(i_perm)
        
    return output

print(diStringMatch("IDID"))