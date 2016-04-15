
#GC content-- python function

def GCcontent(seq)
    for base in seq:
        dic[base] = dic.get(base,0) + 1
    GCcontent = (float(dic["G"]) + dic["C"])/(dic["G"] + dic["A"] + dic["T"] + dic["C"] )
    return GCcontent
    
    
    

