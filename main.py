from pybricks.parameters import Button, Color

from pybricks.tools import multitask, run_task, wait
from robot import hub, drive, left_drive, left_attach
from run1 import run1
from run2 import run2
from run3 import run3
from sweeper import sweeper
from across_the_table import accross_the_table
from tip_the_scales_a import tip_the_scales_a
from tip_the_scales_b import tip_the_scales_b
from whats_on_sale import whats_on_sale
from minecart import minecart
from heavy_lifting import heavy_lifting
from statue import statue

hub.system.set_stop_button((Button.LEFT, Button.RIGHT))


async def center_button_pressed_task():

    while Button.CENTER in hub.buttons.pressed():
        await wait(15)

    while True:
        if Button.CENTER in hub.buttons.pressed():
            return
        await wait(100)


async def switcher(run_list: Dict):
    hub.light.on(Color.ORANGE)
    min_run_number = min(run_list.keys())
    max_run_number = max(run_list.keys())
    current_run_number = min_run_number
    default_drive_settings = drive.settings()
    while True:
        hub.display.number(current_run_number)
        pressed_buttons = hub.buttons.pressed()
        if Button.LEFT in pressed_buttons:
            if current_run_number == min_run_number:
                current_run_number = max_run_number
            else:
                current_run_number -= 1
            while Button.LEFT in hub.buttons.pressed():
                await wait(15)
        if Button.RIGHT in pressed_buttons:
            if current_run_number == max_run_number:
                current_run_number = min_run_number
            else:
                current_run_number += 1
            while Button.RIGHT in hub.buttons.pressed():
                await wait(15)
        if Button.CENTER in pressed_buttons:
            drive.reset()
            drive.settings(*default_drive_settings)
            hub.light.on(Color.GREEN)
            drive.use_gyro(True)

            await multitask(
                run_list[current_run_number](), center_button_pressed_task(), race=True
            )
            drive.stop()
            hub.light.on(Color.ORANGE)
            left_attach.stop()
            while Button.CENTER in hub.buttons.pressed():
                await wait(15)
        await wait(25)


run_list = {}
run_list.update({1: minecart})
run_list.update({2: run2})
run_list.update({3: run3})
run_list.update({4: statue})
run_list.update({5: tip_the_scales_b})
run_list.update({6: run1})
run_list.update({7: whats_on_sale})
run_list.update({8: heavy_lifting})
run_list.update({9: run1})
run_list.update({10: heavy_lifting})
run_list.update({11: sweeper})
run_task(switcher(run_list))
