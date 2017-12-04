
from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import optparse
import subprocess
import random
import traci



THISDIR = os.path.dirname(__file__)
try:
    sys.path.append(os.path.join(os.path.dirname(
        __file__), '..', '..', '..', '..', "tools"))  # tutorial in tests
    sys.path.append(os.path.join(os.environ.get("SUMO_HOME", os.path.join(
        os.path.dirname(__file__), "..", "..", "..")), "tools"))  # tutorial in docs
    from sumolib import checkBinary

except ImportError:
    sys.exit(
        "please declare environment variable 'SUMO_HOME' as the root directory of"
        " your sumo installation (it should contain folders 'bin', 'tools' and 'docs')")

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

def run():
   step = 0

   while step < 10000:
        traci.simulationStep()
        step += 1

   traci.close()
   sys.stdout.flush()

def get_options():
    """define options for this script and interpret the command line"""
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options


# this is the main entry point of this script
if __name__ == "__main__":
    # load whether to run with or without GUI
    options = get_options()
    # If this script has been called from the command line. It will start sumo as a
    # server, then connect and run
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    sumoCmd = [sumoBinary, "-c", "testing/thisisthefile.sumo.cfg"]

    traci.start(sumoCmd)

    run()








