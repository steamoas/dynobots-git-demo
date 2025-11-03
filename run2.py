from robot import drive,left_attach
async def run2():
#left_attach.run_until_stalled(-100, duty_limit=50);
    await drive.curve(62.4,95)
    await drive.straight(274)
    await drive.straight(-200)
    await drive.turn(-90)
    await drive.straight(150)
    await drive.turn(90)
    await drive.straight(400)
