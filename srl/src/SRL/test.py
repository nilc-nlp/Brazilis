#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import sys
import codecs

from SRL import SRLClassifier
from bin.srl.main import load_models


if __name__ == "__main__":
    # Get file ...
    try: 
        fileName = sys.argv[1]
    except IndexError:
        msg = "Enter a file name, e.g. \"python test.py something.txt\""
        raise NameError(msg)
    # Read file ...
    f = codecs.open(fileName, 'r', 'UTF-8')
    sentences = [item.strip() for item in f.readlines()]
    f.close()
    # Loading models ...
    AI_model, AC_model = load_models()
    # Initialize SRLClassifier
    clf = SRLClassifier(sentences, AI_model, AC_model)
    # Print all annotated sentences
    for item in clf.annotated_sentences:
	print item.encode('utf-8')
