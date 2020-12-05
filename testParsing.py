def parseDuneTest(string):
    stack = 0
    lastPoint=0
    tests=[]
    string=string[1:-1]
    for i, c in enumerate(string):
        if c == '[':
            stack+=1
        elif c == ']' and stack>0:
            stack-=1
        elif c==';' and stack == 0:
            tests.append(string[lastPoint:i])
            lastPoint=i+1
    tests.append(string[lastPoint:i+1])
    result=[]
    for e in tests:
        stack = 0
        base=10000
        for i, c in enumerate(e):
            if c == '(':
                stack+=1
            elif c == ')' and stack:
                stack-=1
            elif c == ',' and stack<base:
                base=stack
        if base > 1:
            continue
        elif base==1:
            e = e[1:-1]
        stack = 0
        lastPoint = 0
        param=[]
        #print(e)
        for i, c in enumerate(e):
            if c == '(':
                stack+=1
            elif c == ')' and stack:
                stack-=1
            elif c == ',':
                if stack==0:
                    param.append(e[lastPoint:i])
                    if param[0].count("(") != param[0].count(")"):
                        if len(param)==1 or len(param[-1]) == 0:
                            print("Error parenthese=>",e,param)
                            break
                        param[0]=param[0][1:]
                        param[-1]=param[-1][:-1]
                    #print(param)
                    result.append([param,e[i+1:]])
                    break
                elif stack == 1:
                    param.append(e[lastPoint:i])
                    lastPoint=i+1
    return result
def createTestOcamlPrint(name,list):
    for e in list[0]:
        name+=" ("+e+")"
    return "let testDune = "+name+" in if testDune = ("+list[1]+') then print_string "[OK]'+name+' = '+list[1]+'\\n" else print_string "[ERROR]'+name+' <> '+list[1]+'\\n";;'
def createTestOcamlBool(name,list):
    for e in list[0]:
        name+=" ("+e+")"
    return name+" = ("+list[1]+');;'

#parseDuneTest("[(2,true);(3,true);(5,true);(7,true);(11,true);(13,true);(4,false);(6,false);(12,false);(45,false);(77,false);(63,false)]")
#parseDuneTest("[((2,[2;4;8;12]),true);((11,[2;4;5;20]),true);((23,[2;9;15;18]),true);((29,[30;41;52]),true);((4,[2;9;15;18]),false);((22,[30;41;52]),false);((15,[2;9;15;18]),false);((27,[30;41;52]),false)]")