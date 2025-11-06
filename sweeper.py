# Author: Rodney
# setup: 1.1 left wheel red
# mission number: 1

from pybricks.tools import run_task
from robot import drive

async def sweeper():
    await drive.straight(650)
    await drive.straight(-625)



if __name__ == "__main__":
    run_task(sweeper())
