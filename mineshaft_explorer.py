# setup:2.0 left wheel red
# mission3
# by Rodney


from pybricks.tools import run_task, wait
from robot import drive, left_attach

async def mineshaft_explorer():

    await drive.straight()

if __name__== "__main__":
    run_task(mineshaft_explorer())
