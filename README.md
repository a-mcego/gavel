# Gavel

## What is it?

Gavel is a free and open-source program for practicing foreign language through sentence training.

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

The sentence format is \*.mp3 and \.txt.
There are several tags that can be used in the text file;

* audio, tells the audio path or timestamps in a long file
* target, transcription of the audio
* source, translation of the audio
* ipa, a transcript of the audio in the International Phonetic Alphabet (e.g. /bɔ̃.ʒuʁ/)
* gloss, a morphological analysis
* tag, for arbitrary tagging

For example:
```
tennis.mp3 "Mon frère et moi sommes des bons joueurs de tennis."
tennis.txt
  Mon frère et moi sommes des bons joueurs de tennis.
  My brother and I are good tennis players.
```

A text doesn't have to be split into individual sentence files.
In this case, sentence boundaries and text are defined as follows:
```
tedtalk.mp3
tedtalk.txt
  @line 0.0 1.86
  bonjour et bienvenus à mon TED talk
  good day and welcome to my TED talk
```

Sentences come in folder.
A folder contains *description.txt* where metadata can be stored.
Lines to be supported:

* type:  either sentences or text, if type=text, the sentences as a group will be treated as a text that will become available in the user's "text library" once all the sentences have gone through the regime
* description:   free form text between quotes "" which acts as a short description that will be shown to the user what the text is about, or what the sentence pack is supposed to do, for example "Russian verbs of motion training"
* author:   information about the author
* copyright:   who owns the copyright, in case of paid sentence packs or texts

(amount of sentences for integrity check?)

Example:
```
description.txt
  type=text
  description="A short conversation at the doctor's office"
  author="The Defense Language Institute"
  copyright="Public Domain"
```
