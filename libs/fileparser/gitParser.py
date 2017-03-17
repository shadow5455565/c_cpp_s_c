def gitParser(text, target):
    if target == "updater":
        updates = {
            "BS-online-version":"",
            "VBS-online-version":"",
            "updater-online-version":"",
            }
        x_comma=0
        x=0
        while x < len(text):
            _dir=""
            _version=""
            if text[x]==" ":
                x+=1
            if text[x]=="~":
                while text[x]!=";":
                    x+=1
            else:
                while text[x-2] != ";" and x < len(text):
                    if x_comma!=1:
                        while text[x]!=",":
                            if x < len(text) and text[x]!=" " and text[x]!=";":
                                _dir+=text[x]
                                x+=1
                            else:
                                x+=1
                        x_comma=1
                        x+=1
                    else:
                        if x < len(text) and text[x] != " " and text[x]!=";":
                            _version+=text[x]
                            x+=1
                        else:
                            x+=1
                x_comma=0
                print(_dir +" : "+ _version)
                if _dir=="/libs/startup/updater.py":
                    updates["updater-online-version"]=_version
                if x < len(text):
                    x+=-2
            x+=1
        return updates

##TESTS: uncomment to test the function
"""
updates={
    "BS-online-version":"",
    "VBS-online-version":"",
    "updater-online-version":""
    }
updates2={
    "BS-online-version":"",
    "VBS-online-version":"",
    "updater-online-version":"122"
    }
updates=gitParser("/libs/startup/updater.py ,129;sciao,;", "updater")
print(updates)
if updates2==updates:
    print("Workin well...")
else:
    print("Not same version^^")"""
