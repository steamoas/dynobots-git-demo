from pybricks.tools import multitask, run_task, wait
from robot import drive,right_attach,left_attach

async def run3():
    await drive.straight(750)
    await left_attach.run_target(100,-70)
if __name__ == "__main__":
    run_task(run3())
