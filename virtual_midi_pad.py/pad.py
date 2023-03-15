import pygame.midi

# Initialize Pygame MIDI
pygame.midi.init()

# Define the number of buttons in each row and column
NUM_BUTTONS_PER_ROW = 4
NUM_BUTTONS_PER_COLUMN = 4

# Define the size of each button in pixels
BUTTON_SIZE = 50

# Define the MIDI output port
midi_out = pygame.midi.Output(0)

# Define the MIDI notes to be sent when a button is pressed
midi_notes = [
    [60, 62, 64, 65],
    [67, 69, 71, 72],
    [74, 76, 77, 79],
    [81, 83, 84, 86]
]

# Define the colors of the buttons when they are not pressed and when they are pressed
BUTTON_COLOR = (255, 255, 255)
BUTTON_PRESSED_COLOR = (128, 128, 128)

# Initialize the Pygame display
screen = pygame.display.set_mode((NUM_BUTTONS_PER_ROW * BUTTON_SIZE, NUM_BUTTONS_PER_COLUMN * BUTTON_SIZE))

# Create a list to keep track of which buttons are currently pressed
pressed_buttons = [[False] * NUM_BUTTONS_PER_ROW for _ in range(NUM_BUTTONS_PER_COLUMN)]

# Function to draw the buttons on the screen
def draw_buttons():
    for i in range(NUM_BUTTONS_PER_ROW):
        for j in range(NUM_BUTTONS_PER_COLUMN):
            if pressed_buttons[j][i]:
                color = BUTTON_PRESSED_COLOR
            else:
                color = BUTTON_COLOR
            pygame.draw.rect(screen, color, (i * BUTTON_SIZE, j * BUTTON_SIZE, BUTTON_SIZE, BUTTON_SIZE))
    
    pygame.display.update()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            button_row = y // BUTTON_SIZE
            button_column = x // BUTTON_SIZE
            if not pressed_buttons[button_row][button_column]:
                midi_out.note_on(midi_notes[button_row][button_column], 127)
            pressed_buttons[button_row][button_column] = True

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            button_row = y // BUTTON_SIZE
            button_column = x // BUTTON_SIZE
            if pressed_buttons[button_row][button_column]:
                midi_out.note_off(midi_notes[button_row][button_column], 127)
            pressed_buttons[button_row][button_column] = False

    draw_buttons()

# Clean up Pygame MIDI
pygame.midi.quit()