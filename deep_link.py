import os

adb = 'adb shell am start -W -a android.intent.action.VIEW -d "https://clickotine.com/m/access_code?code=SOME_CODE"'
os.system(adb)