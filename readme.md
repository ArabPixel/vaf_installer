# Vue After Free Installer 

## Usage 
```
git clone https://github.com/Vuemony/vaf_installer/
cd vaf_installer
chmod +x deploy.sh
./deploy.sh 
```

then after it is done building it will output 

```
Save file in /deploy/savedata/localstorage.aes
Serving installer on <your ip address>:42069...
```

1. Download the [Release Zip](https://github.com/Vuemony/vaf_installer/releases/latest) and unzip to root of a USB Drive formatted as exfat
2. Replace `/PS4/APOLLO/11695c49_CUSA00960_localstorage.aes/localstorage.aes` with one generated in `/deploy/savedata/localstorage.aes`
3. Plug USB in to the console
4. Open Apollo Save Tool
5. USB Saves > Application Data (CUSA00960) > Copy Save Game To HDD > Press OK
6. PS Button to go home > Settings > Application Saved Data Management > Saved Data In System Storage > Copy To USB > PS Vue > Check Mark Application Data > Copy.
7. Open Vue
8. Wait 10 seconds

open Playstation Vue

Follow on screen instructions

## Public Server Save file 

optionally the files are hosted remotely and the save has been already generated in [releases](https://github.com/Vuemony/vaf_installer/releases/latest)

simply install it with Apollo Save Tool and create a backup in Settings > Save Data Management
