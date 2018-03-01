"""
Record sound and play it back after a delay.
"""

import multiprocessing as mp
import time
import pyaudio
import numpy
import pygame.mixer
#import matplotlib.pyplot as plt



CHUNK = 1024
CHANNELS = 1
RATE = 44100
DELAY_SECONDS = 5
DELAY_SIZE = DELAY_SECONDS * RATE / (10 * CHUNK)


def feed_queue(q):


    FORMAT = pyaudio.paInt16
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    while True:
        frame = []
        for i in range(10):

            frame.append(stream.read(CHUNK))
        data_ar = numpy.fromstring(b''.join(frame), 'int16')
        if q.full():
            q.get_nowait()
        q.put(data_ar)


queue = mp.Queue(maxsize= int(DELAY_SIZE))
p = mp.Process(target=feed_queue, args=(queue,))
p.start()

# give some time to bufer
time.sleep(DELAY_SECONDS)

pygame.mixer.init()
S = pygame.mixer.Sound
while True:
    print("Loading Queue...")
    d = queue.get()
    ## Processing goes here...


    # Play the sound
    print("Playing audio...")
    S(d).play()