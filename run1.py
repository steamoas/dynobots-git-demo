from pybricks.tools import run_task
from robot import drive,right_attach
async def run1():

    await right_attach.run_target(300,0)

    await drive.straight(
        750)
    await drive.turn(-90)
    await right_attach.run_target(300,0)
    await drive.turn(90)
    await right_attach.run_target(300,-90)
    await drive.straight(1)
    await drive.turn(-70)

if __name__ == "__main__":
    run_task(run1())
