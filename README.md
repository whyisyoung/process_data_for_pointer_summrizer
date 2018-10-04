Forked from: https://github.com/abisee/cnn-dailymail


This code produces the non-anonymized version of the CNN / Daily Mail summarization dataset, as used in the ACL 2017 paper *[Get To The Point: Summarization with Pointer-Generator Networks](https://arxiv.org/pdf/1704.04368.pdf)*. It processes the dataset into the binary format expected by the [code](https://github.com/abisee/pointer-generator) for the Tensorflow model.

**Python 3 version**: This code is in Python 2. If you want a Python 3 version, see [@becxer's fork](https://github.com/becxer/cnn-dailymail/).

# Option 1: download the processed data
User @JafferWilson has provided the processed data, which you can download [here](https://github.com/JafferWilson/Process-Data-of-CNN-DailyMail). (See discussion [here](https://github.com/abisee/cnn-dailymail/issues/9) about why we do not provide it ourselves).

# Option 2: process the data yourself

## 1. Download data
Download and unzip the `stories` directories from [here](http://cs.nyu.edu/~kcho/DMQA/) for both CNN and Daily Mail. 

**Warning:** These files contain a few (114, in a dataset of over 300,000) examples for which the article text is missing - see for example `cnn/stories/72aba2f58178f2d19d3fae89d5f3e9a4686bc4bb.story`. The [Tensorflow code](https://github.com/abisee/pointer-generator) has been updated to discard these examples.

## 2. Download Stanford CoreNLP
We will need Stanford CoreNLP to tokenize the data. Download it [here](https://stanfordnlp.github.io/CoreNLP/) and unzip it. Then add the following command to your bash_profile:
```
export CLASSPATH=/path/to/stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0.jar
```
replacing `/path/to/` with the path to where you saved the `stanford-corenlp-full-2016-10-31` directory. You can check if it's working by running
```
echo "Please tokenize this text." | java edu.stanford.nlp.process.PTBTokenizer
```
You should see something like:
```
Please
tokenize
this
text
.
PTBTokenizer tokenized 5 tokens at 68.97 tokens per second.
```
## 3. Process into .bin and vocab files
The run process is in two parts.

Part 1, run
```
python json_to_hash.py  -f < .json file> -o <output dir>
```

This takes in a JSON file (-f) assuming there are tags “URL” and article body “Sentences” in the JSON.
For each URL, a unique hash is made from the URL. 
For the respective article with that URL, makes a file: <hash>.story
These .story files are written to the output directory (-o)
All the URLs are written to the file: all_urls.txt, one per line.

Part 2, run

```
python make_test_datafiles.py <data_stories_dir> <story type: train.bin, test.bin, or val.bin>
```

This takes in a directory <data_stories_dir> which contains the articles in <hash>.story format and creates a .bin with the provided name: train.bin, test.bin, or val.bin.
Tokenized stories are written to the directory: `tokenized_stories`.
NOTE: If the tokenized_stories directory exists, it must be empty before running this command!
Additionally, a `vocab` file is created from the training data. This is also placed in `finished_files`.
Lastly, <story type: train.bin, test.bin, or val.bin> will be split into chunks of 1000 examples per chunk. These chunked files will be saved in `finished_files/chunked` as e.g. `train_000.bin`, `train_001.bin`, ..., `train_287.bin`. This should take a few seconds. You can use either the single files or the chunked files as input to the Tensorflow code (see considerations [here](https://github.com/abisee/cnn-dailymail/issues/3)).
