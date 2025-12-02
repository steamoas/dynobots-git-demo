# setup:2.0 left wheel red
# mission4
# by Rodney & David


from pybricks.tools import run_task, wait
from robot import drive, left_attach

async def careful_recovery():
    await left_attach.run_angle(300,-170)
    #await drive.straight(850)

if __name__== "__main__":
    run_task(careful_recovery())
