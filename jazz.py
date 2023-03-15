import mido
from mido import Message, MidiFile, MidiTrack

# Set up output port to send MIDI messages to a synthesizer or DAW
out_port = mido.open_output(0)

# Define some basic note durations and velocities
note_on = 0x90
note_off = 0x80
velocity = 64
quarter_note = 60000 / 160  # 160 BPM

# Define a list of instruments to use
instruments = [0, 40, 56, 61]  # Piano, Electric Bass, Trumpet, Tenor Sax

# Define the melody as a list of note numbers
melody = [60, 62, 64, 65, 67, 69, 71, 72]

# Create a new MIDI file with four tracks
midi_file = MidiFile(type=1)
tracks = [MidiTrack() for _ in range(4)]
for track in tracks:
    midi_file.tracks.append(track)

# Add the melody to the first track using the first instrument
for i, note in enumerate(melody):
    tracks[0].append(Message(note_on, note=note, velocity=velocity, time=i*quarter_note))
    tracks[0].append(Message(note_off, note=note, velocity=velocity, time=(i+1)*quarter_note))

# Add a bassline to the second track using the second instrument
bassline = [36, 38, 40, 41, 43, 45, 47, 48]
for i, note in enumerate(bassline):
    tracks[1].append(Message(note_on, note=note, velocity=velocity, time=i*quarter_note))
    tracks[1].append(Message(note_off, note=note, velocity=velocity, time=(i+1)*quarter_note))

# Add a trumpet melody to the third track using the third instrument
trumpet_melody = [68, 70, 71, 73, 75, 77, 78, 80]
for i, note in enumerate(trumpet_melody):
    tracks[2].append(Message(note_on, note=note, velocity=velocity, time=i*quarter_note))
    tracks[2].append(Message(note_off, note=note, velocity=velocity, time=(i+1)*quarter_note))

# Add a saxophone melody to the fourth track using the fourth instrument
sax_melody = [73, 75, 77, 79, 80, 82, 84, 85]
for i, note in enumerate(sax_melody):
    tracks[3].append(Message(note_on, note=note, velocity=velocity, time=i*quarter_note))
    tracks[3].append(Message(note_off, note=note, velocity=velocity, time=(i+1)*quarter_note))

# Save the MIDI file and send the MIDI messages to the output port
midi_file.save('pop_song.mid')
for track in tracks:
    for msg in track:
        out_port.send(msg)