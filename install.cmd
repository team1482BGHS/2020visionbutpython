py -3 -m pip install pip --upgrade

# other vendor libraries such as robotpy-rev are not required to be installed locally
py -3 -m pip install --upgrade robotpy-installer pyfrc pynetworktables

py -3 -m robotpy_installer download-robotpy
py -3 -m robotpy_installer download-opkg robotpy-rev cscore

py -3 -m robotpy_installer install-robotpy
py -3 -m robotpy_installer install-opkg robotpy-rev cscore