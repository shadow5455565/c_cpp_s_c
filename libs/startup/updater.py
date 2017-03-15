import urrlib.request as url
import libs.variables.VBootStrapper.VBootStrapper as VBootStrapper
class updater:
    commands{
      "Check-Updates" : "check-updates"
    };
    def check_updates:
        htmlonlinefilelist=url.urlopen("https://www.github.com/shadow5455565/c_cpp_s_c/onlinefilelist.txt").read()
        onlinefilelist=parseFile(htmlonlinefilelist, "HTML/dbtx")
        txtlocalfilelist=open("/localfilelist.txt", "r+").read()
        localfilelist=parseFile(txtlocalfilelist, "TXT/dbtx")
        VBootStrapper.updates = listcompariser(onlinefilelist, localefilelis, "different")
        txtlocalfilelist.close()
    def update(comm):
        updater.commands[comm]()
        
