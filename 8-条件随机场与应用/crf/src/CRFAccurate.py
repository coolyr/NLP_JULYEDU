#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# File: CRFAccurate.py
# Date: 14/Mar/2016
# Desc: calculate the accuracy of the crf_test output
#
# Produced By CSRGXTU
import sys
from Utility import loadCrfMatrixFromFile

if len(sys.argv) != 2:
  print 'Usage: CRFAccurate.py result.log'
  sys.exit(1)

inputFile = sys.argv[1]

mat = loadCrfMatrixFromFile(inputFile)
total = 0
hit = 0
for row in mat:
  if len(row) == 1:
    continue

  total = total + 1
  if row[-1] == row[-2]:
    hit = hit + 1

print float(hit)/total 