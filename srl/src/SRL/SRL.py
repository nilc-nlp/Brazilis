#!/usr/bin/env python
#-*- encoding:utf-8 -*-

# SRL.py - Semantic role labeling algorithm described by Alva-Manchego [2013]
#
# Copyright (C) 2015  SAMSUNG Eletrônica da Amazônia LTDA
#
# Authors:  Alessandro Bokan Garay <alessandro.bokan@gmail.com>
#           Nathan Siegle Hartmann <nathanshartmann@gmail.com> (creator of
#           the SRL models)

import re
import os
import sys
sys.path.append('src')

from utils.run_palavras import (run_palavras_sentence_by_web_service,
                                add_semantic_tags)
from utils.CONLL import annotate_instance
from utils.insert_subject import insert_first_person_subj 
from utils.anota_verbo_conll import anota_verbo_conll, anota_auxiliares_conll
from utils.subject_fixer import subject_fixer
from utils.srl_auxiliary_verbs import insert_auxiliary_verbs
from corpus.util.CoNLLFormatter import main
from corpus.util.PropsPrinter import props_printer
from bin.srl.main import classify


class SRLClassifier():
    def __init__(self, sentences, AI_model, AC_model):
        self.argident_sys, self.argclass_sys = AI_model, AC_model
        self.annotated_sentences = self.annotate(sentences)

    def annotate(self, sentences):
        annotated_sentences = []
        # Iterate all sentences
        for sentence in sentences:
            # Sentence pre-processing
            sentence = re.sub('[\"|\[|\]]', '', sentence).strip()
            # Initialize "annotated_sentence"
            annotated_sentence = sentence
            # Run PALAVRAS TigerXML. Get a list of words of the sentence
            try:
		xml_file = run_palavras_sentence_by_web_service(sentence)
		insert_first_person_subj(xml_file)
		subject_fixer(xml_file)
                words = add_semantic_tags(xml_file)
		insert_auxiliary_verbs()
            except:
                annotated_sentences.append(annotated_sentence)
                continue
            # If exists a list of words (or a syntactic tree has nonterminals
            # and has verbs)
            if words:
                try:
                    # Transform TigerXML to CoNLL format
                    main()
		    props_printer()
                    # Semantic Role Labelling (SRL)
                    classify(self.argident_sys, self.argclass_sys)
		    anota_verbo_conll()
		    anota_auxiliares_conll()
                    # Get sentence annotated with "semantic roles"
                    annotated_sentence = annotate_instance(words[0])
                except:
                    pass
            # Append sentences
            annotated_sentences.append(annotated_sentence)
        # Return all sentences anotated "semantic roles"
        return annotated_sentences
