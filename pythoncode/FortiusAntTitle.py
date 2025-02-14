#-------------------------------------------------------------------------------
# Version info
#-------------------------------------------------------------------------------
WindowTitle = "Fortius Antifier v6.7" # Double quotes, see below!
# 2022-12-28    Version 6.7     #404 BLE does not work when debug=0
#                               #404 PowerFactor setting always reset to 20
# 2022-08-24    Version 6.7     #341 Refactoring of ANT reading loop
# 2022-08-16    Version 6.6     #152 Zwift steering implemented
# 2022-08-10    Version 6.5     #366 BLE-bless released
# 2022-04-14    Version 6.4     #366 BLE-bless; #360 #361 #362 #363 #373 #379
# 2022-01-04    Version 6.3     Issues 340, 342, 353 implemented
# 2021-03-23    Version 6.2     Leds also for GUI, Raspberry TFT display
# 2021-03-17    Version 6.1     Vortex Quality Improvement
# 2021-03-17    Version 6.0     major change: Raspberry integrated!
# 2021-01-25    Version 5.2     Issues #189, #216, #222
# 2021-01-21    Version 5.1     Published
#                               settings can be modified interactively
#                               #120 font/rear changing
#                               #195 power changing from headunit
# 2021-01-04                    master branch (5.0) merged into 4.2 Quality upgrade branch
# 2021-01-04    Version 5.0     #117 Tacx Bushido and #101 Genius implemented
# 2020-12-20    Version 4.2     #173 Version 4.0 Communicates Much Higher Power vs. 3.8
#                               #184 Power in Rouvy issue
# 2020-12-20    Version 4.1.1   #137 Improvements for Raspberry PI
# 2020-12-20    Version 4.1.c   #103 Implement Bluetooth support
# 2020-12-15    Version 4.1.b   #147 Improve run-off procedure
#                               #164 Ignore headunit buttons
# 2020-12-14    Version 4.1.a   #121 Implementation of ANT+ Remote control
# 2020-12-11    Version 4.0     Implementation of Magnetic Brake on "USB"
# 2020-11-19    Version 3.8
# 2020-11-18    Version 3.7
# 2020-11-12    Version 3.6
# 2020-11-05    Version 3.5
# 2020-11-04    First version
#-------------------------------------------------------------------------------
import debug
import logfile
import time
import urllib.request

#-------------------------------------------------------------------------------
# g i t h u b W i n d o w T i t l e
#-------------------------------------------------------------------------------
# input:        WindowTitle
#				The published version on github
#
# description:  Check whether github uploaded version is different from ourselves
#
# output:		none
#
# returns:      WindowTitle [version on github=WindowTitle]
#-------------------------------------------------------------------------------
def githubWindowTitle():
    rtn = WindowTitle
    url = 'https://raw.githubusercontent.com/WouterJD/FortiusANT/master/pythoncode/FortiusAntTitle.py'

    try:
        file = urllib.request.urlopen(url)
    except:
        if debug.on(debug.Function):
            logfile.Write ('No access to FortiusAntTitle.py on github')
        pass
    else:
        if debug.on(debug.Function):
            logfile.Write ('Check FortiusAntTitle.py on github')
        for line in file:
            DecodedLine = line.decode('utf-8')

            if DecodedLine[:len('WindowTitle')] == 'WindowTitle':
                #---------------------------------------------------------------
                # We read ourselves, so second token must be WindowTitle
                #---------------------------------------------------------------
                githubWindowTitle = DecodedLine.split('"')[1]
                #---------------------------------------------------------------
                # Check if equal; unequal is considered newer
                #---------------------------------------------------------------
                if debug.on(debug.Any):
                    logfile.Write ('Version='+ WindowTitle + ', on github=' + githubWindowTitle + '.')
                if githubWindowTitle == WindowTitle:
                    pass
                else:
                    rtn = rtn + ' [version on github=' + githubWindowTitle + ']'
                break
        file = None
    return rtn

#-------------------------------------------------------------------------------
# Main program to test the previous functions
#-------------------------------------------------------------------------------
if __name__ == '__main__':
    t1 = time.time()
    print(githubWindowTitle())
    t2 = time.time()
    print('Executed in %5.3f seconds' % (t2 - t1))