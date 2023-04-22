def list(l):
    return l

def long(l,min_length):
    ll=[]
    for ele in l:
        if(len(ele)>min_length):
            ll.append(ele)
    return ll

