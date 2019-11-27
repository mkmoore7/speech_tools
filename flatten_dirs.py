import os
import argparse
import shutil

def flatten(data_dir, save_dir):
    r = []
    for root, dirs, files, in os.walk(data_dir):
        for name in files:
            shutil.move(os.path.join(root, name), os.path.join(save_dir, name))
            print(name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='utility to flatten the VCTK toolkit')
    parser.add_argument('--data_loc')
    parser.add_argument('--flat_loc')
    args = parser.parse_args()

    flatten(args.data_loc, args.flat_loc)
