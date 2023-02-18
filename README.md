# Text to chord bot

This is a [Telegram](http://telegram.org) bot to turn a chord into a sound (`.wav`) file -- just to add a little dramatic atmosphere for the chatting.

## Feature

- Turn texts of chord names into sounds and send back
- Allow designating pitch of the root 
- Allow input of a group of notes to form a customized chord (TODO)

## Usage

- Add @TextToChordBot to group chat
- To create a chord by chord name, use "`\d` + Chord name", for example "`\d Cmaj7`" for major seventh on C
- To create a chord by name with a root pitch, use "`\d` + Chord name + integer pitch", for example, "`\d Cmaj7 4`" for major seventh on C4.

Note that the bot is only available when I start its service.

## Dependencies and config

The code is written in Python with the following dependencies:

`pychord                   1.1.1`
`pretty-midi               0.2.9`
`midi2audio                0.1.1`
`pytelegrambotapi          4.10.0`

To create your own text to chord bot, put your TeleBot token under a file named `config.ini`.