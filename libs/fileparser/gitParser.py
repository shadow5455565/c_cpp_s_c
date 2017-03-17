###PART OF THE PROJECT C/C++ Script Checker###

###SYNTAX of the online filelist and local filelist:
### "<ignore>directory, version;" where <ignore> is ~ if we want to ignore the string
### like ~/dir/example.py, 1.0.0; , this string is ignored and it passes to the next one
### /dir/example2.py, 1.0.2;, this is not ignored and variable _dir will be "/dir/example2.py" and _varsion will be "1.0.2"
###CREATED by CRYogen aka shadow5455565, for contacts raulradu2000@yahoo.it | twitter @shadow5455565 | github: github.com/shadow5455565
###This is free to use and modify, just give me credits.
###Have a nice reading and understanding of the code, and a nice day ^^
###Again if you want to implement new functionalities to the code and perfectionate it just write me an email with the new parts,
###and i'll add them to the code giving you credits

###TODO: 1. Create a function that clears the file by the \n and other things like that;
###      2. Add dir checker for BS-online-version;
###      3. Add dir checker fo  VBS-online-version;
###      4. Add offline-file parser;
###      5. Port variable updates in function gitParser() to a more global location, 
###         like a class with all the update variables(/libs/variables/VBootStrap.py);

### Variable text is the input text coming, target is the variable, or better dictionary, where the parsed output is going
def gitParser(text, target):
    if target == "updater-online": ###for the online version of the file
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
updates=gitParser("/libs/startup/updater.py ,129;sciao,;", "updater-online")
print(updates)
if updates2==updates:
    print("Workin well...")
else:
    print("Not same version^^")"""
