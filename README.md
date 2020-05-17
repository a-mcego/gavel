# Gavel

## What is it?

Gavel is a free and open-source program for practicing foreign language through sentence training.
Through the tagging feature it can also be used for linguistic research.

## Implemented features

* loads sentences into memory
* allows the user to listen and transcribe sentences

## Planned features

Gavel has *activities* that can be organized into *regimes*.
An activity is for example transcription.
A regime consists of activities that can be hierarchically organized, such that once a sentence is transcribed, it is available for the next activity.
Support is planned for whole texts, so once all the sentences for a text have gone through the regime the fulltext becomes available to the learner.
The program will also track the user's progress per language and activity, and display that.
For example "You have transcribed 265 French sentences."

Gavel comes with one regime of three activities by default:

1. transcription
2. chorus training
3. translation

Transcription allows the user to loop a sentence indefinitely while transcribing on a separate medium, preferably a notebook.
The user can then reveal the correct transcription, and if the user managed to transcribe the sentence, they can move that sentence forward in the regime.
If it was too difficult, the user can return the sentence back to the group of sentences awaiting transcription.

Chorus training also allows the user to loop the sentence indefinitely.
The user will be instructed to try to pronounce the sentence simultaneously with the recording.

Translation shows the user the sentence in translation (line 2 from the .txt), and prompts the user to translate it in a manner they see fit.
They can for example say the sentence out loud in the target language as fast as they can (forced recall), translate it by hand on a notebook or type it in a text field in the program.
The user's translation will then be displayed next to the correct one, and the user is prompted for failure (returns the sentence back to the "to be translated" pile) or success, which marks the sentence as complete.

## Format

A pack of sentences always comes in a folder with audio files and *sentences.txt*.
Each sentence is declared with a line that says 'sentence' (simple enough).

The tags that *sentences.txt* contains;

* audio, tells the audio path or timestamps in a long file
* target, transcription of the audio
* source, translation of the audio
* ipa, a transcript of the audio in the International Phonetic Alphabet (e.g. /bɔ̃.ʒuʁ/)
* gloss, a morphological analysis
* tag, for arbitrary tagging

A sentence needs audio, target and source, otherwise the sentence will fail to load.

Example:
```
tennis.mp3
sentences.txt
  sentence
  audio tennis.mp3 0:00 2:32
  target Mon frère et moi sommes des bons joueurs de tennis.
  source My brother and I are good tennis players.
  tag tense=present speaker=male mood=indicative
  sentence
  audio tennis.mp3 2:32 3:90
  target Mon frère il s'appelle Jacques.
  source My brother's name is Jacques.
  gloss 1sg-poss.m.sg HE 3refl-CALL.3sg-pres-ind JACQUES
  tag verb=reflexive
```

The folder also contains *description.txt* where metadata is stored:

* type, either sentences or text, if type=text, the sentences as a group will be treated as a text that will become available in the user's 'text library' once all the sentences have gone through the regime
* title, the title of the text or sentence pack
* target, the ISO 639-3 code for the target language (https://en.wikipedia.org/wiki/ISO_639-3)
* source, the ISO 639-3 code for the source language
* description, free form text which acts as a short description that will be shown to the user what the text is about, or what the sentence pack is supposed to do, for example 'Russian verbs of motion training'
* author, information about the author
* copyright, copyright license
* tag, for arbitrary tagging

Example:
```
description.txt
  type text
  title At the doctor's office
  target fra
  source eng
  description A short conversation at the doctor's office
  author The Defense Language Institute (DLI)
  copyright Public Domain
  tag dialogue
```
