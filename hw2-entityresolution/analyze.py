import pandas as pd
import string_distance as strdis
import decimal
import re

print("starting")

def get_google_catalog():
    count = 0
    goog_df = pd.read_csv('GoogleProducts.csv', encoding = 'unicode_escape')
    goog_df = goog_df.fillna("")
    #goog_df = goog_df.head(20)
    glist = goog_df.values.tolist()
    return glist

def get_amazon_catalog():
    amaz_df = pd.read_csv('Amazon.csv', encoding = 'unicode_escape')
    amaz_df = amaz_df.fillna("")
    #amaz_df = amaz_df.head(20)
    alist = amaz_df.values.tolist()
    return alist

def read_file(filename):
	tlist = []
	data = open(filename, 'r')
	lines = data.readlines()
	for line in lines:
		tlist.append(line.strip())
	return tlist

stopwords = set(read_file("stopwords.txt"))
print(stopwords)

def rem_dup(ls):
    res = []
    for i in ls:
        if i not in res:
            res.append(i)
    return res

def jaccard_str(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    div = len(s1.union(s2))
    if div == 0:
        return 0
    return float(len(s1.intersection(s2)) / len(s1.union(s2)))

def remove_noise(str):
    str = str.replace("-","")
    str = str.replace(":","")
    str = str.replace(".","")
    str = str.replace("!","")
    str = str.replace("/","")
    str = str.replace("(","")
    str = str.replace(")","")
    str = str.replace("[","")
    str = str.replace("]","")
    str = str.replace("}","")
    str = str.replace("{","")
    str = str.replace("&","")
    str = str.replace("1","")
    str = str.replace("2","")
    str = str.replace("3","")
    str = str.replace("4","")
    str = str.replace("5","")
    str = str.replace("6","")
    str = str.replace("7","")
    str = str.replace("8","")
    str = str.replace("9","")
    str = str.replace("0","")
    str = str.replace("'","")
    str = str.replace("software","")
    str = str.replace("adobe","")
    str = str.replace("microsoft","")
    #stack overflow re.sub

    query = str
    query = str.lower()
    querywords = query.split()

    resultwords  = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    
    return result

def frange(x, y, jump=1.0):
    i = 0.0
    x = float(x)
    x0 = x
    epsilon = jump / 2.0
    yield x 
    while x + epsilon < y:
        i += 1.0
        x = x0 + i * jump
        if x < y:
          yield x

def ret_best(ls):
    best = [0,0]
    for i in ls:
        if i[1] > best[1]:
            best.pop(0)
            best.pop(0)
            best.append(i[0])
            best.append(i[1])

    return best

def contains(lg,sm):
    lg = re.split('\s+', lg)
    sm = re.split('\s+', sm)
    count = 0
    for i in sm:
        for x in lg:
            if i == x:
                #print(x, " | ", i)
                count = count + 1
    return count / len(sm)


# END OF HELPERS ======================================================
'''
def sim(a,g):
    miss = 0
    count = 0 
    ret = []

    #===== title simularity =====
    title_sim = jaccard_str(remove_noise(g[1]),remove_noise(a[1]))
    if title_sim > 0.76:
        count = count + 1
    else:
        ret.append(0)
        ret.append(0)
        return ret

    #===== manufacture simularity =====
    manu_sim = 0
    if len(a[3]) > 0 and len(g[3]) > 0:
        print("A:",a[3]," G:",g[3])
        manu_sim = strdis.levenshtein(g[3],a[3])
        manu_sim = manu_sim / 100
    else:
        manu_sim = 0
    

    #===== price simularity =====
    if type(g[4]) is str:
        g[4] = g[4].replace("gbp", "")
    pg = float(g[4])
    pa = float(a[4])
    if pa != 0 and pg != 0:
        diff = abs(pg-pa)
        diff = diff / 100
    else:
        diff = 0

    #===== final count =====
    if count  == 1:
        ret.append(g[0])
        ret.append((10 * title_sim) - diff)
        return ret
    else:
        ret.append(0)
        ret.append(0)
        return ret
'''

def sim(a,g):
    miss = 0
    count = 0 
    ret = []

    #===== title simularity =====
    glen = len(g[1])
    alen = len(a[1])
    tg = remove_noise(g[1])
    ta = remove_noise(a[1])


    #===== price simularity =====
    if type(g[4]) is str:
        g[4] = g[4].replace("gbp", "")
    pg = float(g[4])
    pa = float(a[4])
    if pa != 0 and pg != 0:
        diff = abs(pg-pa)
        diff = diff / 900
    else:
        diff = 0

   #===== manufacture simularity =====
    manu_sim = 0
    if len(a[3]) > 0 and len(g[3]) > 0:
        manu_sim = strdis.levenshtein(g[3],a[3])
        manu_sim = manu_sim / 1000
    else:
        manu_sim = 0
    
    #===== final count =====
    if alen > glen:
        if contains(ta,tg) >= 0.52:
            print(ta," | ", tg)
            ret.append(g[0])
            ret.append(jaccard_str(remove_noise(g[1]),remove_noise(a[1])) - diff - manu_sim)
            return ret
    elif glen > alen:
        if contains(tg,ta) >= 0.52:
            print(tg, " | ", ta)
            ret.append(g[0])
            ret.append(jaccard_str(remove_noise(g[1]),remove_noise(a[1])) - diff - manu_sim)
            return ret
    else:
        ret.append(0)
        ret.append(0)
        return ret
    ret.append(0)
    ret.append(0)
    return ret

def match():

    count = 0
    goog = get_google_catalog()
    amaz = get_amazon_catalog()
    matched_pairs = []

    for a in amaz:
        bucket = []
        for g in goog:
            simul = sim(a,g)
            if simul[0] != 0:
                bucket.append(simul)
                count = count + 1
                print(count)
        g = ret_best(bucket)
        matched_pairs.append((a[0],g[0]))

    print("total matches: ", len(matched_pairs))
    return matched_pairs
    '''
    count = 0
    goog = get_google_catalog()
    amaz = get_amazon_catalog()
    matched_pairs = []

    for a in amaz:
        bucket = []
        for g in goog:
            simul = sim(a,g)
            if simul[0] != 0:
                count = count + 1
                print(count)

                g[0] = simul[0]

                matched_pairs.append((a[0],g[0]))

    print("total matches: ", len(matched_pairs))
    return matched_pairs
    '''
