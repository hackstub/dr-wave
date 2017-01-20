'''
ftp://ftp.renci.org/outgoing/astro_app/Python/Lib/site-packages/pygame/_numpysndarray.py
'''

import pygame, numpy, math

duration = 1.0          # in seconds
sample_rate = 44100
bits = 16

pygame.mixer.init(frequency = sample_rate, size = -bits, channels = 2)

n_samples = int(round(duration*sample_rate))
buf = numpy.zeros((n_samples, 2), dtype = numpy.int16)
max_sample = 2**(bits - 1) - 1

def mod_amp_tri(t):
	if t < 0.5: return t
	else: return 1-t

def mod_amp_sin(t):
	return (math.sin(t*13))/2

def fn_square(t):
	if math.ceil(t)%2 == 0: return 1.0
	else: return 0.0

for s in range(n_samples):
	t = float(s)/sample_rate        # time in seconds
	print(fn_square(t/2.0))
	buf[s][0] = int(round(max_sample*math.sin(2*math.pi*440*t)*fn_square(t))) # left
	buf[s][1] = buf[s][0]    # right

sound = pygame.sndarray.make_sound(buf)
sound.play()

pygame.time.wait(int(round(1000*duration)))

pygame.mixer.quit()
