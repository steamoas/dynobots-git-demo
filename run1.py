from pybricks.tools import multitask, run_task, wait
from robot import drive,right_attach
async def run1():

    await right_attach.run_target(300,0)

    await drive.straight(
        750)

    await right_attach.run_target(300,90)
    await multitask(
        drive.turn(-40),
        wait(1500),
        race=True
    )

    await drive.straight(-750)





if __name__ == "__main__":
    run_task(run1())
