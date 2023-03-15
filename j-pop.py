import pygame
import pygame.midi

# Initialize Pygame and Pygame MIDI
pygame.init()
pygame.midi.init()

# Set the window size
WINDOW_SIZE = (800, 600)

# Set the title of the window
pygame.display.set_caption("Energetic Animated Song with Pygame")

# Open a new window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Define the font for the lyrics
font = pygame.font.Font(None, 36)

# Set the tempo of the song
tempo = 120

# Open the default MIDI output port
port = pygame.midi.Output(pygame.midi.get_default_output_id())

# Set the program (sound) to "Distortion Guitar"
port.set_instrument(30)

# Define the notes of the melody
notes = [60, 64, 67, 69, 72, 74, 76, 77]

# Define the rhythm of the melody
rhythm = [2, 2, 2, 1, 1, 1, 1, 2]

# Define the lyrics
lyrics = ["Energetic,",
          "Animated,",
          "Feel the beat and",
          "Move your feet!"]

# Define the colors for the lyrics
colors = [pygame.Color("red"),
          pygame.Color("green"),
          pygame.Color("blue"),
          pygame.Color("yellow")]

# Define the position of the lyrics
x = 0
y = WINDOW_SIZE[1] - font.get_height()

# Define the animation speed
speed = 5

# Set the time signature to 4/4
pygame.time.set_timer(pygame.USEREVENT, int(60 * 1000 / tempo))

# Start the main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            # Play the melody
            for i in range(len(notes)):
                # Turn the note on
                port.note_on(notes[i], 127)
                # Wait for the duration of the note
                pygame.time.wait(int(60 * rhythm[i] / tempo * 1000))
                # Turn the note off
                port.note_off(notes[i], 127)
            # Move the lyrics up
            y -= speed
            if y < -font.get_height():
                y = WINDOW_SIZE[1]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Stop the program (sound)
            port.all_notes_off()
    # Draw the background
    screen.fill(pygame.Color("white"))
    # Draw the lyrics
    for i in range(len(lyrics)):
        text = font.render(lyrics[i], True, colors[i % len(colors)])
        screen.blit(text, (x, y + i * font.get_height()))
    # Update the screen
    pygame.display.flip()

# Close the MIDI output port
port.close()

# Quit Pygame and Pygame MIDI
pygame.quit()
pygame.midi.quit()