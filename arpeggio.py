import pygame.midi

# Initialize Pygame MIDI
pygame.midi.init()

# Open the default MIDI output port
port = pygame.midi.Output(pygame.midi.get_default_output_id())

# Set the program (sound) to "Acoustic Guitar (nylon)"
port.set_instrument(25)

# Define the notes of the C major arpeggio
notes = [60, 64, 67, 72]

# Define the duration of each note in milliseconds
duration = 200

# Set the velocity (volume) of each note
velocity = 100

# Play the arpeggio repeatedly
while True:
    for note in notes:
        # Turn the note on
        port.note_on(note, velocity)
        # Wait for the duration of the note
        pygame.time.wait(duration)
        # Turn the note off
        port.note_off(note, velocity)
    # Wait for a short break before repeating the arpeggio
    pygame.time.wait(duration)

# Close the MIDI output port
port.close()

# Quit Pygame MIDI
pygame.midi.quit()