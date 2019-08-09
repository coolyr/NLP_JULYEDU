#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# Date: 12/Mar/2016
# File: PrepareTrainingData.py
# Desc: preparing the training data for CRF++
#
# Format: each row is a token, consist of the following
# GameName HomeAway FGM FGA 3PM 3PA FTM FTA OREB DREB AST TOV STL BLK PF PTS WinLose
#
# Produced By CSRGXTU
import sys

from Utility import loadMatrixFromFile, saveCrfMatrix

if len(sys.argv) != 2:
  print 'Usage: PrepareTrainingData.py teamid'
  sys.exit(1)

teamid = sys.argv[1]

DATA_PATH = '../data/TeamRank/'

mat = loadMatrixFromFile(DATA_PATH + teamid + '.csv.sorted')

trainMat = []
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

  trainMat.append(tmp)

TrainMat = []
for i in range(len(trainMat)):
  if i == len(trainMat) - 5:
    break
  TrainMat.append(trainMat[i])
  TrainMat.append(trainMat[i + 1])
  TrainMat.append(trainMat[i + 2])
  TrainMat.append(trainMat[i + 3])
  TrainMat.append(trainMat[i + 4])
  TrainMat.append(trainMat[i + 5])
  TrainMat.append([])


saveCrfMatrix(DATA_PATH + teamid + '.train.csv', TrainMat[0:-99])
