#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# Date: 12/Mar/2016
# File: PrepareTrainingData6.py
# Desc: preparing the training data for CRF++, 6 nearest as average
#
# Format: each row is a token, consist of the following
# GameName HomeAway FGM FGA 3PM 3PA FTM FTA OREB DREB AST TOV STL BLK PF PTS WinLose
#
# Produced By CSRGXTU
import sys

from Utility import loadMatrixFromFile, saveCrfMatrix, loadTeamRanks

if len(sys.argv) != 2:
  print 'Usage: PrepareTrainingData6.py teamid'
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

  # TeamRank
  # According season, open TeamRank file and store it in tmp
  # tmp.append(loadTeamIds(DATA_PATH + mat[i][2] + '.l')[8])
  # print DATA_PATH + mat[i][2] + '.l'
  # print loadTeamRanks(DATA_PATH + mat[i][2] + '.l')[0][8]
  tmp.append(loadTeamRanks(DATA_PATH + mat[i][2] + '.l')[0][8])
  # sys.exit(0)

  trainMat.append(tmp)



# print trainMat[0:6]
for i in range(10):
  print trainMat[i]

print '#####'

for i in range(len(trainMat) - 6):
# for i in range(10 - 6):
  # tmp = []
  HA = trainMat[i][1] + trainMat[i + 1][1] + trainMat[i + 2][1] + trainMat[i + 3][1] + trainMat[i + 4][1] + trainMat[i + 5][1]
  FGM = int(trainMat[i][2]) + int(trainMat[i + 1][2]) + int(trainMat[i + 2][2]) + int(trainMat[i + 3][2]) + int(trainMat[i + 4][2]) + int(trainMat[i + 5][2])
  FGA = int(trainMat[i][3]) + int(trainMat[i + 1][3]) + int(trainMat[i + 2][3]) + int(trainMat[i + 3][3]) + int(trainMat[i + 4][3]) + int(trainMat[i + 5][3])
  ThreePM = int(trainMat[i][4]) + int(trainMat[i + 1][4]) + int(trainMat[i + 2][4]) + int(trainMat[i + 3][4]) + int(trainMat[i + 4][4]) + int(trainMat[i + 5][4])
  ThreePA = int(trainMat[i][5]) + int(trainMat[i + 1][5]) + int(trainMat[i + 2][5]) + int(trainMat[i + 3][5]) + int(trainMat[i + 4][5]) + int(trainMat[i + 5][5])
  FTM = int(trainMat[i][6]) + int(trainMat[i + 1][6]) + int(trainMat[i + 2][6]) + int(trainMat[i + 3][6]) + int(trainMat[i + 4][6]) + int(trainMat[i + 5][6])
  FTA = int(trainMat[i][7]) + int(trainMat[i + 1][7]) + int(trainMat[i + 2][7]) + int(trainMat[i + 3][7]) + int(trainMat[i + 4][7]) + int(trainMat[i + 5][7])
  OREB = int(trainMat[i][8]) + int(trainMat[i + 1][8]) + int(trainMat[i + 2][8]) + int(trainMat[i + 3][8]) + int(trainMat[i + 4][8]) + int(trainMat[i + 5][8])
  DREB = int(trainMat[i][9]) + int(trainMat[i + 1][9]) + int(trainMat[i + 2][9]) + int(trainMat[i + 3][9]) + int(trainMat[i + 4][9]) + int(trainMat[i + 5][9])
  AST = int(trainMat[i][10]) + int(trainMat[i + 1][10]) + int(trainMat[i + 2][10]) + int(trainMat[i + 3][10]) + int(trainMat[i + 4][10]) + int(trainMat[i + 5][10])
  TOV = int(trainMat[i][11]) + int(trainMat[i + 1][11]) + int(trainMat[i + 2][11]) + int(trainMat[i + 3][11]) + int(trainMat[i + 4][11]) + int(trainMat[i + 5][11])
  STL = int(trainMat[i][12]) + int(trainMat[i + 1][12]) + int(trainMat[i + 2][12]) + int(trainMat[i + 3][12]) + int(trainMat[i + 4][12]) + int(trainMat[i + 5][12])
  BLK = int(trainMat[i][13]) + int(trainMat[i + 1][13]) + int(trainMat[i + 2][13]) + int(trainMat[i + 3][13]) + int(trainMat[i + 4][13]) + int(trainMat[i + 5][13])
  PF = int(trainMat[i][14]) + int(trainMat[i + 1][14]) + int(trainMat[i + 2][14]) + int(trainMat[i + 3][14]) + int(trainMat[i + 4][14]) + int(trainMat[i + 5][14])
  PTS = int(trainMat[i][15]) + int(trainMat[i + 1][15]) + int(trainMat[i + 2][15]) + int(trainMat[i + 3][15]) + int(trainMat[i + 4][15]) + int(trainMat[i + 5][15])
  WinLose = trainMat[i][16] + trainMat[i + 1][16] + trainMat[i + 2][16] + trainMat[i + 3][16] + trainMat[i + 4][16] + trainMat[i + 5][16]
  # tmp.append([HA, FGM/6, FGA/6, ThreePM/6, ThreePA/6, FTM/6, FTA/6, OREB/6, DREB/6, AST/6, TOV/6, STL/6, BLK/6, PF/6, PTS/6, WinLose])
  # print tmp
  trainMat[i + 6] = [trainMat[i + 6][0], trainMat[i + 6][1], FGM/6, FGA/6, ThreePM/6, ThreePA/6, FTM/6, FTA/6, OREB/6, DREB/6, AST/6, TOV/6, STL/6, BLK/6, PF/6, PTS/6, trainMat[i + 6][17], trainMat[i + 6][16]]
  print trainMat[i + 6]
  # for j in range(1, len(trainMat[i])):
  #   #   print j
  #     tmp.append(trainMat[i][j] + trainMat[i + 1][j] + trainMat[i + 2][j] + trainMat[i + 3][j]
  #     + trainMat[i + 4][j] + trainMat[i + 5][j])
  #     print tmp
  # trainMat[i + 6] = tmp

# for i in range(10):
    # print trainMat[i]
for i in range(6):
    res = trainMat[i][16]
    tr = trainMat[i][17]
    trainMat[i][16] = tr
    trainMat[i][17] = res

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


saveCrfMatrix(DATA_PATH + teamid + '.test6tr.csv', TrainMat[-99:])
