# Gavel

## What is it?

Gavel is a free and open-source program for practicing foreign language through sentence training.

## Features

Gavel has *activities* that can be organized into *regimes*.
An activity is for example transcription.
A regime consists of activities that can be hierarchically organized, such that once a sentence is transcribed, it is available for the next activity.
Support is planned for whole texts, so once all the sentences for a text have gone through the regime the fulltext becomes available to the learner.

Gavel comes with one regime of three activities by default:

1. transcription
2. chorus training
3. translation

Transcription allows the user to loop a sentence indefinitely while transcribing on a separate medium, preferably a notebook.
The user can then reveal the correct transcription, and decide 

## Format

The sentence format is \*.mp3 and \.txt.
In the text file, the first line is the transcript and the second like is its translation and all notes that might be necessary.

For example
```
tennis.mp3 "Mon frère et moi sommes des bons joueurs de tennis."
tennis.txt
  Mon frère et moi sommes des bons joueurs de tennis.
  My brother and I are good tennis players.
```
Sentences come in folder.
A folder contains *description.txt* where metadata can be stored.
Lines to be supported:

* type:  either sentences or text, if type=text, the sentences as a group will be treated as a text that will become available in the user's "text library" once all the sentences have gone through the regime
* description:   free form text between quotes "" which acts as a short description that will be shown to the user what the text is about, or what the sentence pack is supposed to do, for example "Russian verbs of motion training"
* author:   information about the author
* copyright:   who owns the copyright, in case of paid sentence packs or texts

Example:
```
description.txt
type=text
description="A short conversation at the doctor's office"
author="The Defense Language Institute"
copyright="Public Domain"
```
