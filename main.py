import sys
import time
from dataprep.dataPrep import callDataPrep
from openrefine.openRefine import callOpenRefine
from createwikidataitems.finalPrepareStep import createWikidataItems


def timerCountdownPrint(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("Time Remaining: {0}".format(i))
        time.sleep(1)
    sys.stdout.write("\r\rTime up...\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Lets Us Create Wikidata Items.")
    ready4orFile = callDataPrep()
    callOpenRefine(ready4orFile)

    continueCode = str(input("Write \'continue\' to continue to create wikidata items or \'exit\' to exit now: "))
    if continueCode.lower() == 'continue':
        createWikidataItems()
    else:
        print("Exiting...")
        exit(0)


# SAMPLE INPUT

# /Users/sprasad/Documents/SDSU/CAL/
# Q7413726
# Q35069
# Q101028767
# https://womensstudies.sdsu.edu/people/
# N
# women
# cal_women_tenure
# /Users/sprasad/Documents/chromedriver
# yes
# t
# 'C:/Users/sprasad/Documents/SDSU/CAL/women/cal-women-tenure-ready4bot.csv'
# 'C:/Users/sprasad/Documents/SDSU/CAL/women/final/cal-women-tenure.csv'
