crf
===

conditional random field

#### Training the crf model
```bash
../bin/bin/crf_learn template-file ../data/TeamRank/1610612757.train.csv model-file
```

### Testing the crf model
```bash
../bin/bin/crf_test -m model-file ../data/TeamRank/1610612757.test.csv > result.log
```

### Calculate the accuracy
```bash
./CRFAccurate.py result.log
```