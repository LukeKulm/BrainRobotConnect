""" SSVEP 4-Image Speller

################################# DESCRIPTION #################################

This module will allow a patient with motor impairment to instruct their 
healthcare robot to retrieve certain objects they need in daily life, without
the need to speak or move their limbs or fingers.

The four commands include: water, medicine, food, and book. Each command 
will be represented as a flashing image, each with a different flashing 
frequency. We will detect the Steady-State Visual Evoked Potential (SSVEP), 
an event related potential in EEG data that is evoked by visual stimuli that
are presented at a specific frequency. It results in an increase in the EEG
at that same frequency. When participants direct their attention to these 
stimuli, this increases the EEG response at the stimulus frequency 
(Joon Kim et al., 2007). If the patient directs their attention towards the 
water image that is flashing at say 15Hz, then the 15Hz component in the 
patient's EEG response will increase.

The script will have two states, resting and active. The resting stage will
be triggered by the patient closing their eyes for a prolonged moment (10s), 
during which alpha waves increase in power. The flashing of images stop in 
the resting stage. The active stage will also be triggered by the same 
prolonged closing eye event, and the images will flash.

"""

import time
import copy
import random
import sys
import numpy as np
from psychopy import visual, core, data, event, gui

## Experiment
def experiment(monitor="testMonitor", path=""): 
    
    clock = core.Clock()
    monitor_Hz = 60
    
    # define display window
    win = visual.Window(fullscr=True, color="black", units='cm', monitor=monitor)
    
    # read images
    water_im = 'water.jpeg'
    food_im = 'food.jpeg'
    medicine_im = 'medicine.jpeg'
    book_im = 'book.jpeg'
    black_im = 'black.png'
    images = [water_im, food_im, medicine_im, book_im]
    
    # define frequencies
    frequencies = [6, 10, 15, 30]
    
    # message to indicate the active state is switched on
    passage = "You have now turned on the active state.\nPlease stare at the image that contains the object you want the robot to bring to you.\nPlease wait 3 seconds to be directed to the speller."
    show_text(win, passage, clock, 0.5, 3)
    win.flip()
    
    # set up image display
    positions = [(0.8, 0.8), (0.8, -0.8), (-0.8, 0.8), (-0.8, -0.8)]
    print('reached positions')
    frames_to_show = [10, 6, 4, 2] # frames on and off respectively
    water_stim = visual.ImageStim(win, image=images[0], pos=positions[0], units="norm")
    food_stim = visual.ImageStim(win, image=images[1], pos=positions[1], units="norm")
    medicine_stim = visual.ImageStim(win, image=images[2], pos=positions[2], units="norm")
    book_stim = visual.ImageStim(win, image=images[3], pos=positions[3], units="norm")
    stim = [water_stim, food_stim, medicine_stim, book_stim]
    # create black stimulations for each of the four corners
    black_stim = []
    for corner in np.arange(4):
        black_stim.append(visual.ImageStim(win, image=black_im, pos=positions[corner], units="norm"))
    
    flip = [-1,-1,-1,-1]
    
    while 'q' not in event.getKeys():
        for frameN in range(60):
            for im in range(4):
                if frameN % frames_to_show[im] == 0:
                    flip[im] *= -1
                if flip[im] == 1:
                    stim[im].draw()
                    win.flip(clearBuffer = False)
                else: 
                    black_stim[im].draw()
                    win.flip(clearBuffer = False)

def show_text(win, text, clock, fontSize, passageDur):
    textStim = visual.TextStim(win, text=text, height=fontSize, alignText='left', color='white', wrapWidth=20)
    textStim.draw()
    win.flip()
    core.wait(passageDur)

def main():
    experiment()

if __name__ == "__main__":
    main()
    
