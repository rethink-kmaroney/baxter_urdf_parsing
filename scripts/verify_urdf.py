#!/usr/bin/env python

import sys
import argparse

from urdf_parser_py.urdf import URDF

parser = argparse.ArgumentParser(usage='Load an URDF file')
parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=None, help='File to load. Use - for stdin')
parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=None, help='Dump file to XML')
args = parser.parse_args()

if args.file is None:
    print 'VERIFYING FROM PARAM SERVER'
    robot = URDF.from_parameter_server()
else:
    print 'VERIFYING FROM STRING'
    robot = URDF.from_xml_string(args.file.read())

print(robot)
print "ALL IS WELL! URDF PASSED PARSING!"

if args.output is not None:
    args.output.write(robot.to_xml_string())
