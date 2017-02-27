#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gbkim
#
# Created:     11-02-2017
# Copyright:   (c) gbkim 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import tqdm
    import time

    for i in tqdm.tqdm(range(int(1000))):
        time.sleep(0.01)


if __name__ == '__main__':
    main()
