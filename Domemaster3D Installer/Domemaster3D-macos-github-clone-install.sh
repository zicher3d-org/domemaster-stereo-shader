#! /bin/sh

echo "Domemaster3D macOS GitHub Clone Install"
echo "----------------------------------------------------------"
echo "by Andrew Hazelden <andrew@andrewhazelden.com>"
echo "2016-12-08 10.00 AM"
echo ""


# BASH text colors
RED='\033[0;31m'
NONE='\033[00m'

# Check if the script was run as root with sudo
if [ "$EUID" -ne 0 ]; then
  printf "${RED}[ERROR] This script requires root privileges to run.\n\n"
  printf "${NONE}Try launching the script again with:\n"
  printf "sudo sh ./Domemaster3D-macos-github-clone-install.sh\n"
  printf "\n\n"
  exit
fi

# Check if the Domemaster3D installation folder exists
if [ -d "/Applications/Domemaster3D" ]; then

  # Clear out the old /Applications/Domemaster3D folder
  echo "[Domemaster3D] Removing the old installation located at: /Applications/Domemaster3D"
  rm -rf "/Applications/Domemaster3D"
fi

# Install the Domemaster3D files
echo "[Domemaster3D] Installing the GitHub files"
mkdir -p "/Applications/Domemaster3D/"
cp -R "$HOME/Documents/GitHub/domemaster-stereo-shader/Domemaster3D Installer/installer files/Domemaster3D/" "/Applications/Domemaster3D/"

echo "[Domemaster3D] Setting up the user permissions"
chmod -R 777 "/Applications/Domemaster3D/"


# Install the Domemaster3D Maya shelves
echo "[Domemaster3D] Installing the Maya 2017 shelves"
mkdir -p "$HOME/Library/Preferences/Autodesk/maya/2017/prefs/shelves/"
cp "$HOME/Documents/GitHub/domemaster-stereo-shader/Domemaster3D Installer/installer files/Domemaster3D/maya/2017/shelves/shelf_Domemaster3D.mel" "$HOME/Library/Preferences/Autodesk/maya/2017/prefs/shelves/"

cp "$HOME/Documents/GitHub/domemaster-stereo-shader/Domemaster3D Installer/installer files/Domemaster3D/vray/maya/shelves/shelf_VRayDomemaster3D.mel" "$HOME/Library/Preferences/Autodesk/maya/2017/prefs/shelves/"

cp "$HOME/Documents/GitHub/domemaster-stereo-shader/Domemaster3D Installer/installer files/Domemaster3D/arnold/mtoa/shelves/shelf_ArnoldDomemaster3D.mel" "$HOME/Library/Preferences/Autodesk/maya/2017/prefs/shelves/"

echo "[Domemaster3D] Setting up the Maya 2017 shelf permissions"
chmod -R 777 "$HOME/Library/Preferences/Autodesk/maya/2017/modules/"


# Install the Domemaster3D Maya module files
echo "[Domemaster3D] Installing the Maya 2017 Modules"
mkdir -p "$HOME/Library/Preferences/Autodesk/maya/2017/modules/"

cp "$HOME/Documents/GitHub/domemaster-stereo-shader/Domemaster3D Installer/installer files/Domemaster3D/maya/modules/Domemaster3D-mr3.14.mod" "$HOME/Library/Preferences/Autodesk/maya/2017/modules/"

cp "$HOME/Documents/GitHub/domemaster-stereo-shader/Domemaster3D Installer/installer files/Domemaster3D/vray/maya/modules/VRayDomemaster3D.mod" "$HOME/Library/Preferences/Autodesk/maya/2017/modules/"

cp "$HOME/Documents/GitHub/domemaster-stereo-shader/Domemaster3D Installer/installer files/Domemaster3D/arnold/mtoa/modules/ArnoldDomemaster3D.mod" "$HOME/Library/Preferences/Autodesk/maya/2017/modules/"

echo "[Domemaster3D] Setting up the Maya 2017 modules permissions"
chmod -R 777 "$HOME/Library/Preferences/Autodesk/maya/2017/modules/"


echo "[Domemaster3D] Installation Done."
sleep 2
