import libs.startup.update as update
import libs.globals as globals
class startup:
   def startup():
      print("Checking for updates...", end=" ")
      globals.updates= update.update("Check-Updates")
      if globals.updates["BS_New_version"]==1:
         print("(!) New version ("+ updates["BS-Version"] + ") of the BootStapper!")
         print("(!) Downloading the new version...", end="")
         update.update("BS-update") ## in update.update: gitdownload("shadow5455565", "c_cpp_s_c") ## (author, repository name)
         print("[ DONE ]")
      else:
         print("(-) The BootStrapper is already updated.")
      if globals.updates["CSA_New_version"]==1:
         print("(!) New version (" + updates["CSA_version"] + ") of the C Script Analyzer available...")
         print("(!) Downloading the new version...", end="")
         update.update("CSA-Update")
               
