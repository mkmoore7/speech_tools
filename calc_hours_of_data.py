import numpy as np
import os
import librosa
import argparse

def main():
    parser = argparse.ArgumentParser(description='Calculate the number of hours of audio in a given directory')
    parser.add_argument('--directory' )

    args= parser.parse_args()
    directory = args.directory

    seconds = 0

    for filename in os.listdir(directory):
        print(filename)
        #Check that it's an audio file
        ext = filename.split('.')[-1]
        if ext in ['wav', 'mp3']:  #add more extensions here if necessary
            y, sr = librosa.load(os.path.join(directory,filename))
            seconds = seconds + len(y)/sr
    print('There are {} seconds of audio in this directory'.format(seconds))
    print('There are {} minutes of audio in this directory'.format(seconds/60.0))
    print('There are {} hours of audio in this directory'.format(seconds/3600.0))
if __name__ == '__main__':
    main()
