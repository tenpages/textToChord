import tempfile
from pychord import Chord
import pretty_midi
import midi2audio

note_to_number = {'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 6, 'B': 7}

def createChord(input: str) -> Chord:
    chord = Chord(input)
    return chord

def parseRequest(req: str) -> str:
    cmd = req.split(" ")
    if len(cmd) <= 1:
        return -1
    if cmd[0] == '/d':
        chord = createChord(cmd[1])
        sound = createSound(chord, int(cmd[2]))
        return sound
    if cmd[0] == '/c':
        return parseChord(cmd[1:])
    return ""

def createSound(chord: Chord, root_pitch: int = 3, length: int = 1) -> str:
    midi_data = pretty_midi.PrettyMIDI()
    midi_pointer = tempfile.mkstemp()
    wav_pointer = tempfile.mkstemp()
    piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
    piano = pretty_midi.Instrument(program=piano_program)

    for note_name in chord.components_with_pitch(root_pitch = root_pitch):
        note_number = pretty_midi.note_name_to_number(note_name)
        note = pretty_midi.Note(velocity=100, pitch=note_number, start=0, end=length)
        piano.notes.append(note)
    midi_data.instruments.append(piano)
    midi_data.write(midi_pointer[1])

    fs = midi2audio.FluidSynth()
    fs.midi_to_audio(midi_pointer[1], "test.wav")

    return wav_pointer[1]

def parseChord() -> str:
    return ""

if __name__ == "__main__":
    parseRequest("/d Emaj7 4")
