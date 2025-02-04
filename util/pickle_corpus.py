"""
Read training data CSVs from the corpus and serialize the results.

Jesse Mu
"""

import pickle  # Standard pickle for unicode support
import csv
import os


def csv_extract(filename):
    tweets = []
    with open(filename, 'r') as f:
        reader = csv.reader(f, quotechar='"')
        rows = list(reader)
    for row in rows:
        sentiment = row[0]
        text = row[-1]
        # 4 is positive, 2 is neutral, 0 is negative
        if sentiment == '4':
            sentiment = 'positive'
        elif sentiment == '2':
            sentiment = 'neutral'
        elif sentiment == '0':
            sentiment = 'negative'
        else:
            raise Exception(
                "Don't know how to handle sentiment {}".format(sentiment)
            )
        tweets.append([text, sentiment])
    return tweets


def serialize(filename, dictionary, verbose=False):
    """Output to a file or stdout with pickle."""
    with open(filename, 'w') as fout:
        pickle.dump(dictionary, fout)


def pickle_filename(filename):
    assert filename[-4:] == '.csv' and filename[:8] == 'corpora/'
    return 'lib/{}.pickle'.format(filename[8:-4])

if __name__ == '__main__':
    for filename in os.listdir("corpora/"):
        if filename.endswith(".csv"):
            filename = "corpora/{}".format(filename)
            print "parsing {}".format(filename)
            tweets = csv_extract(filename)
            pickle_file = pickle_filename(filename)
            print "writing to {}".format(pickle_file)
            with open(pickle_file, 'w') as fout:
                pickle.dump(tweets, fout)
