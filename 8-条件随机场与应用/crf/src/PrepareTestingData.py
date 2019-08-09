#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# File: PrepareTestingData.py
# Date: 14/Mar/2016
# Desc: prepare testing data from the train file temply
#
# Produced By CSRGXTU
import sys

from Utility import loadMatrixFromFile, saveCrfMatrix

if len(sys.argv) != 2:
  print 'Usage: PrepareTestingData.py teamid'
  sys.exit(1)

teamid = sys.argv[1]

DATA_PATH = '../data/TeamRank/'

mat = loadMatrixFromFile(DATA_PATH + teamid + '.csv.sorted')

testMat = []
for i in range(len(mat)):
  tmp = []
  # GameName
  tmp.append('G' + str(i + 1))
  # HomeAway, home is H, else A
  if '@' in mat[i][5]:
    tmp.append('H')
  else:
    tmp.append('A')
  # FGM
  tmp.append(mat[i][6])
  # FGA
  tmp.append(mat[i][7])
  # 3PM
  tmp.append(mat[i][8])
  # 3PA
  tmp.append(mat[i][9])
  # FTM
  tmp.append(mat[i][10])
  # FTA
  tmp.append(mat[i][11])
  # OREB
  tmp.append(mat[i][12])
  # DREB
  tmp.append(mat[i][13])
  # AST
  tmp.append(mat[i][14])
  # TOV
  tmp.append(mat[i][17])
  # STL
  tmp.append(mat[i][15])
  # BLK
  tmp.append(mat[i][16])
  # PF
  tmp.append(mat[i][18])
  # PTS
  tmp.append(mat[i][19])
  # WinLose
  tmp.append(mat[i][0])

  testMat.append(tmp)

TestMat = []
for i in range(len(testMat)):
  if i == len(testMat) - 5:
    break
  TestMat.append(testMat[i])
  TestMat.append(testMat[i + 1])
  TestMat.append(testMat[i + 2])
  TestMat.append(testMat[i + 3])
  TestMat.append(testMat[i + 4])
  TestMat.append(testMat[i + 5])
  TestMat.append([])


saveCrfMatrix(DATA_PATH + teamid + '.test.csv', TestMat[-99:])
