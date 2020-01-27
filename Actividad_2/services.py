import os
import platform

if platform.system() == 'Windows':
    os.system("sc query state=all > servicios.txt")
    os.system('cmd /k "sc query state= all"')

elif platform.system() == 'Linux':
    os.system("systemctl list-units --all --type=service --no-pager > servicios.txt")
    os.system("systemctl list-units --all --type=service --no-pager")
