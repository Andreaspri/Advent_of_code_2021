with open("data.txt","r") as f:
    collection = {}
    count11=0
    count12=0
    linecount1 = 0
    maincount1 = 0
    f = f.readlines()
    for i in f:
        if i == "\n":
            collection.__delitem__("\n")
            for key,values in collection.items():
                count11+=1
                if values >= linecount1:
                    count12+=1
            collection = {}
            linecount1 = 0
            continue
        elif i[i.__len__()-1] != '\n':
            linecount1+=1
            for temp_char in i:
                if temp_char in collection.keys():
                    value = collection.get(temp_char)
                    value+=1
                    collection.update({temp_char:value})
                else:
                    collection.update({temp_char:1})
                    try: collection.__delitem__("\n")
                    except: pass
            for key,values in collection.items():
                count11+=1
                if values >= linecount1:
                    count12+=1
            collection = {}
            linecount1 = 0
            continue
        linecount1+=1
        for temp_char in i:
            if temp_char in collection.keys():
                value = collection.get(temp_char)
                value+=1
                collection.update({temp_char:value})
            else:
                collection.update({temp_char:1})

print("Part 1: ",count11)
print("Part 2: ",count12)