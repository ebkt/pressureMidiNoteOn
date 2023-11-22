import time          # import time module so we can slow the program a bit
import board         # import board info (pins, etc)
import analogio      # import analogio for analog input
import usb_midi      # import python midi libraries
import adafruit_midi # import adafruit midi library
from adafruit_midi.note_on import NoteOn

pressure = analogio.AnalogIn(board.A0) # create variable to store input from pressure sensor

midi_channel = 1 # set midi channel
midi = adafruit_midi.MIDI(midi_out = usb_midi.ports[1], out_channel = midi_channel-1) # init midi

while True:
    mapped = pressure.value / 65535    # map the input range to 0 to 1
    if mapped > 0.5:                   # if our input is greater than 0.5
        midi.send(NoteOn(1))           # send midi NoteOn message for note number 1
        print(1)                       # print to serial as well (for testing)
    time.sleep(0.1)                    # sleep for 0.2sec to slow the program down a bit