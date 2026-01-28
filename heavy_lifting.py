# setup:1.0 rightwheel blue
# mission7
# by David


from pybricks.tools import run_task, wait
import careful_recovery
from robot import drive, left_attach

async def heavy_lifting():

    await drive.curve(150,100)

if __name__== "__main__":
    run_task(heavy_lifting())
