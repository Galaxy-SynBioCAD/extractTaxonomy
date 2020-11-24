#!/usr/bin/env python3

import argparse
import logging
import sys
sys.path.insert(0, '/home/')

import rpTool


##
#
#
if __name__ == "__main__":
    parser = argparse.ArgumentParser('Generate taxonomy id in a JSON')
    parser.add_argument('-input', type=str)
    parser.add_argument('-output', type=str)
    params = parser.parse_args()
    #sbml read the different mode
    rpTool.getTaxon(params.input, params.output)
