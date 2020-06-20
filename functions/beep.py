def beep():
    import os
    os.system('play -n synth %s sin %s' % (1, 500))

if __name__ == '__main__':
    beep()