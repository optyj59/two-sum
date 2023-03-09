def twoSum(List,target):
    lenList = len(List)
    for i in range(0,lenList-1):
    
        fst = i
        for r in range(fst+1,lenList):
            snd = r
            if(List[fst]+List[snd] == target):
                break;
        if(List[fst]+List[snd] == target):
            break;    
        
    return [fst,snd]
