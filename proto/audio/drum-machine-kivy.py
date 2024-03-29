import pygame
from pyo import *
from time import sleep
from kivy.uix.button import Button

# Constants
BEAT_TIME=.25

# Drum sounds
hihat_file = "sounds/chh37.ogg"
kick_file = "sounds/kick_22.ogg"
side_file = "sounds/sidestick24.ogg"
snare_file = "sounds/snaretop_37.ogg" 

# Drum beat
hihat_presets = [[8, 1, 1, 1, 1, 1, 1, 1, 1],
                 [8, 0, 0, 0, 0, 1, 0, 0, 0]]
kick_preset = [[8, 1, 0, 0, 0, 1, 0, 0, 0]]
side_preset = [[8, 0, 0, 1, 0, 0, 0, 0, 0]]
snare_preset = [[8, 1, 0, 0, 0, 0, 0, 1, 0]]

# Create synchronous callbacks generated by Pyo
server = Server().boot()
server.start()

hihat_beat = Beat(time=BEAT_TIME)
hihat_beat.setPresets(hihat_presets)
hihat_beat.recall(0)
hihat_beat.play()
hihat_table = SndTable(hihat_file)
hihat_out = TrigEnv(hihat_beat, table=hihat_table, dur=hihat_table.getDur(), interp=1, mul=1)

kick_beat = Beat(time=BEAT_TIME)
kick_beat.setPresets(kick_preset)
kick_beat.recall(0)
kick_beat.play()
kick_table = SndTable(kick_file)
kick_out = TrigEnv(kick_beat, table=kick_table, dur=kick_table.getDur(), interp=1, mul=1)

side_beat = Beat(time=BEAT_TIME)
side_beat.setPresets(side_preset)
side_beat.recall(0)
side_beat.play()
side_table = SndTable(side_file)
side_out = TrigEnv(side_beat, table=side_table, dur=side_table.getDur(), interp=1, mul=1)

snare_beat = Beat(time=BEAT_TIME)
snare_beat.setPresets(snare_preset)
snare_beat.recall(0)
snare_beat.play()
snare_table = SndTable(snare_file)
snare_out = TrigEnv(snare_beat, table=snare_table, dur=snare_table.getDur(), interp=1, mul=1)

mixer = Mixer(outs=3, chnls=2, time=.025)
mixer.addInput(0, hihat_out)
mixer.addInput(1, kick_out)
mixer.addInput(2, side_out)
mixer.addInput(3, snare_out)
mixer.setAmp(0,0,.5)
mixer.setAmp(0,1,.5)
mixer.setAmp(1,0,.5)
mixer.setAmp(1,1,.5)
mixer.setAmp(2,0,.5)
mixer.setAmp(2,1,.5)
mixer.setAmp(3,0,.5)
mixer.setAmp(3,1,.5)
mixer.out()

# Evidence that we can PAUSE and PLAY using these callbacks
sleep(5)
server.stop()
sleep(2)
server.start()
sleep(5)

# sleep(5.3)
# print "Recalling next"
# hihat_beat.recall(1)

# server.gui(locals)

# sleep(100)
