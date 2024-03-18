#!/usr/bin/python3

import samin.__main__ as smn
import samin.btrfs
import sys
import argparse

output = ""

for line in sys.stdin:
    str = line.replace("\n", " ")
    output += str

current_root = smn.get_block("/")
current_subvol = samin.btrfs.get_subvolume("/")


parser = argparse.ArgumentParser(description="samin pacman hook script")

parser.add_argument("--pre-install", help="Pre Installation", action="store_true")
parser.add_argument("--post-install", help="Post Installation", action="store_true")
parser.add_argument("--pre-removal", help="Pre Removal", action="store_true")
parser.add_argument("--post-removal", help="Post Removal", action="store_true")


args = parser.parse_args()

if args.pre_install is True:
    action = "Pre-installation: "
if args.post_install is True:
    action = "Post-installation: "
if args.pre_removal is True:
    action = "Pre-removal: "
if args.post_removal is True:
    action = "Post-removal: "

samin.btrfs.take_snapshot(current_subvol, current_root, action + output)
