## import libs.x.class as class where x is a directory
import libs.startup.updater.updater as updater
import libs.variables.VBootStrapper.VBootStrapper as VBootStrapper
class startup:
   def startup():
      print("(*) Checking for updates...", end=" ")
      VBootStrapper.updates = update.update("Check-Updates")
      print("  (*)Checking for new BootStrapper version...")
      if globals.updates["BS_New_version"] == 1:
         print("     (!) New version ("+ VBootStrapper.updates["BS-Version"] + ") of the BootStapper!")
         print("     (!) Downloading the new version...", end="")
         updater.update("BS-update") ## in update.update: gitdownload("shadow5455565", "c_cpp_s_c") ## (author, repository name)
         print(" [ DONE ]")
      else:
         print("     (-) The BootStrapper is already updated.")
      print("  (*)Checking for new C Script Analyzer version...")
      if VBootStrapper.updates["CSA_New_version"] == 1:
         print("     (!) New version (" + VBootStrapper.updates["CSA_version"] + ") of the C Script Analyzer available...")
         print("     (!) Downloading the new version...", end="")
         updater.update("CSA-Update")
         print(" [ DONE ]")
      else:
         print("     (-) The C Script Analyzer is already updated.")
