import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Define the size of the window in pixels
WINDOW_SIZE = (400, 400)

# Define the number of buttons in each row and column
NUM_BUTTONS_PER_ROW = 4
NUM_BUTTONS_PER_COLUMN = 4

# Define the size of each button in pixels
BUTTON_SIZE = 50

# Define the colors of the buttons when they are not pressed, when they are pressed, and when the mouse is over them
BUTTON_COLOR = (255, 255, 255)
BUTTON_PRESSED_COLOR = (128, 128, 128)
BUTTON_HOVER_COLOR = (200, 200, 200)

# Define the MIDI output ports
midi_outs = ["MIDI 1", "MIDI 2", "MIDI 3", "MIDI 4"]

# Initialize the window and the font
window = pygame.display.set_mode(WINDOW_SIZE)
font = pygame.font.SysFont(None, 24)

# Create a NumPy array to keep track of the state of each button
buttons = np.zeros((NUM_BUTTONS_PER_COLUMN, NUM_BUTTONS_PER_ROW), dtype=bool)

# Create a flag to keep track of whether the mouse is over a button
mouse_over_button = False

# Create a variable to keep track of the currently selected MIDI output port
selected_midi_out = None

# Create a function to draw the buttons on the screen
def draw_buttons():
    for i in range(NUM_BUTTONS_PER_ROW):
        for j in range(NUM_BUTTONS_PER_COLUMN):
            button_rect = pygame.Rect(i * BUTTON_SIZE, j * BUTTON_SIZE, BUTTON_SIZE, BUTTON_SIZE)
            if buttons[j][i]:
                pygame.draw.rect(window, BUTTON_PRESSED_COLOR, button_rect)
            elif mouse_over_button and button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(window, BUTTON_HOVER_COLOR, button_rect)
            else:
                pygame.draw.rect(window, BUTTON_COLOR, button_rect)

# Create a function to draw the MIDI output port selection menu on the screen
def draw_midi_out_menu():
    menu_rect = pygame.Rect(0, WINDOW_SIZE[1] - 40, WINDOW_SIZE[0], 40)
    pygame.draw.rect(window, (255, 255, 255), menu_rect)
    menu_text = font.render("Select MIDI output port:", True, (0, 0, 0))
    window.blit(menu_text, (10, WINDOW_SIZE[1] - 30))
    for i, midi_out in enumerate(midi_outs):
        midi_out_text = font.render(midi_out, True, (0, 0, 0))
        midi_out_rect = pygame.Rect(WINDOW_SIZE[0] - 10 - midi_out_text.get_width(), WINDOW_SIZE[1] - 30, midi_out_text.get_width(), 20)
        pygame.draw.rect(window, (200, 200, 200) if selected_midi_out == i else (255, 255, 255), midi_out_rect)
        window.blit(midi_out_text, (WINDOW_SIZE[0] - 10 - midi_out_text.get_width(), WINDOW_SIZE[1] - 30))

# # Run the main loop
# running = True
# while running:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         # elif event.type == pygame.MOUSEBUTTONDOWN:
#         #     if event.button == 1:
#         #         # Left mouse

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
