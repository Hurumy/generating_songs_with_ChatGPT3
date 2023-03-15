import pygame.midi
import random

# Initialize Pygame and Pygame MIDI
pygame.init()
pygame.midi.init()

# Set the tempo (in BPM)
tempo = 160

# Set the duration of the song (in seconds)
duration = 30

# Set the time signature to 4/4
time_signature = (4, 4)

# Set the number of tracks
num_tracks = 3

# Set the number of bars
num_bars = int(duration * tempo / 60 / time_signature[0])

# Set the number of beats per bar
num_beats = time_signature[1]

# Set the resolution (in ticks per beat)
resolution = 96

# Set the MIDI channel for each track
channels = [0, 1, 2]

# Open the default MIDI output port
port = pygame.midi.Output(pygame.midi.get_default_output_id())

# Set the program (sound) for each track
port.set_instrument(0, 0)  # Drums
port.set_instrument(34, 0)  # Bass
port.set_instrument(81, 0)  # Lead

# Define the drum patterns
drum_patterns = [
    [[36], [], [], [], [38], [], [], [], [42], [], [], [], [46], [], [], []],  # Kick, Snare, Hi-hat, Ride
    [[36], [38], [], [], [42], [], [], [], [46], [], [], [], [42], [], [], []],  # Kick, Snare, Hi-hat, Ride
    [[36], [], [42], [], [36], [], [42], [], [36], [], [42], [], [42], [], [42], []],  # Kick, Hi-hat, Snare, Rimshot
]

# Define the bass notes
bass_notes = [48, 50, 52, 53]

# Define the lead notes
lead_notes = [60, 62, 64, 65]

# Define the chord progression
chord_progression = [
    [48, 52, 55],  # C Major
    [50, 54, 57],  # D Major
    [52, 56, 59],  # E Major
    [53, 57, 60],  # F Major
]

# Define the melody pattern
melody_pattern = [
    [1, 1, 1, 1],  # Quarter notes
    [2, 2],  # Half notes
    [1, 1, 2],  # Quarter and half notes
]

# Generate the drum track
for bar in range(num_bars):
    for beat in range(num_beats):
        pattern = random.choice(drum_patterns)
        for track in range(num_tracks):
            for tick in range(resolution):
                for note in pattern[beat]:
                    port.note_on(note, 100, channels[track])
                port.write_short(0x80 | channels[track], 0, 0)
                port.write_short(0xF8, 0, 0)
                # Calculate the time in ticks
                ticks = bar * num_beats * resolution + beat * resolution + tick
                # Wait for the specified amount of time
                pygame.time.wait(int(60000 / tempo / resolution))
                
# Generate the bass track
for bar in range(num_bars):
    # Choose a chord progression for this bar
    chords = random.choice(chord_progression)
    # Choose a bass note for each beat in this bar
    bass = [random.choice(chords) for beat in range(num_beats)]
    for beat in range(num_beats):
        note = bass[beat]
        for tick in range(resolution):
            port.note_on(note, 100, channels[1])
            port.write_short(0x80 | channels[1], 0, 0)
            port.write_short(0xF8, 0, 0)
            pygame.time.wait(int(60000 / tempo / resolution))
            
# Generate the melody track
for bar in range(num_bars):
    # Choose a melody pattern for this bar
    pattern = random.choice(melody_pattern)
    # Choose a lead note for each beat in this bar
    lead = [random.choice(lead_notes) for beat in range(num_beats)]
    for beat in range(num_beats):
        # Determine the duration of the note based on the pattern
        duration = pattern[beat % len(pattern)]
        # Choose a note for the melody
        note = random.choice(chord_progression[beat % len(chord_progression)])
        for tick in range(resolution * duration):
            port.note_on(note, 100, channels[2])
            port.write_short(0x80 | channels[2], 0, 0)
            port.write_short(0xF8, 0, 0)
            pygame.time.wait(int(60000 / tempo / resolution))
            
# Close the MIDI output port
port.close()

# Quit Pygame and Pygame MIDI
pygame.quit()
pygame.midi.quit()