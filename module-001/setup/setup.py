#! /usr/bin/env python

import os
import random
import sys

def random_items(res, count):
    f = open(res, 'r')
    a = f.readlines()
    ret = []
    for i in range(0, count):
	ret.append(random.choice(a))

    return ret

def setup_files(f, ext, count):
    d = os.path.expanduser('downloads')
    a = random_items(f + '.txt', count)
    for item in a:
	if not ext == '':
	    f = open('%s/%s.%s' % (d, item.strip(), ext), 'w')
	else:
	    f = open('%s/%s' % (d, item.strip()), 'w')

def setup_series(f, ext, count):
    d = os.path.expanduser('downloads')
    a = random_items(f + '.txt', count)
    for item in a:
	season = random.randint(1, 3)
	epi = random.randint(1, 24)
	f = open('%s/%s-s%de%d.%s' % (d, item.strip(), season, epi, ext), 'w')

def main(args):
    setup_files('movies', 'avi', 30)
    setup_files('movies', 'mkv', 5)
    setup_series('series', 'avi', 60)
    setup_series('series', 'mkv', 3)
    setup_files('music', 'mp3', 70)
    setup_files('music', 'ogg', 5)
    setup_files('ebooks', 'pdf', 80)
    setup_files('ebooks', 'doc', 4)
    setup_files('ebooks', 'odt', 10)
    setup_files('notes', 'txt', 8)
    setup_files('archives', 'tar.gz', 50)
    setup_files('archives', 'tar.bz2', 1)
    setup_files('archives', 'zip', 20)
    setup_files('junk', '', 70)

if __name__ == '__main__':
    main(sys.argv[1:])
