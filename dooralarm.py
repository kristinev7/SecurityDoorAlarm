#ACTUAL CODE : 
#Sender: 
MagStrength = 0
radio.set_group(7)

def on_forever():
    global MagStrength
    MagStrength = input.magnetic_force(Dimension.STRENGTH)
    if MagStrength < 1750:
        radio.send_number(1)
        basic.show_icon(IconNames.NO)
    else:
        radio.send_number(2)
        basic.show_icon(IconNames.YES)
basic.forever(on_forever)

#Receiver:
def on_received_number(receivedNumber):
    if receivedNumber == 1:
        basic.show_icon(IconNames.ANGRY)
        music.start_melody(music.built_in_melody(Melodies.BA_DING),
            MelodyOptions.FOREVER_IN_BACKGROUND)
        if input.button_is_pressed(Button.A):
            music.stop_all_sounds()
            basic.pause(10000)
    elif receivedNumber == 2:
        basic.show_icon(IconNames.YES)
        music.stop_melody(MelodyStopOptions.ALL)
radio.on_received_number(on_received_number)

radio.set_group(7)

def on_forever():
    if radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH) <= 0:
        basic.show_icon(IconNames.SWORD)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        if input.button_is_pressed(Button.B):
            music.stop_all_sounds()
basic.forever(on_forever)

#LED Receiver 2:
	def on_received_number(receivedNumber):
    if receivedNumber == 3:
        turnOn()
radio.on_received_number(on_received_number)

def turnOn():
    global val
    while val < 1024:
        val = val + 1
        pins.analog_write_pin(AnalogPin.P0, val)
    basic.pause(1000)
    while val > 0:
        val = val – 1
        pins.analog_write_pin(AnalogPin.P0, val)
    basic.pause(1000)
val = 0
led.enable(False)
radio.set_group(7)
