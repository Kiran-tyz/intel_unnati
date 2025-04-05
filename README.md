import pygame, sys
import random
from button import Button
from easyq.easy import generate_easy_mcq

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load(r"C:\Users\taskm\OneDrive\Desktop\ai game\menu.png")
BG = pygame.transform.scale(BG, (1280, 720))

OP = pygame.image.load(r"C:\Users\taskm\OneDrive\Desktop\ai game\Open_Bg.png")
OP = pygame.transform.scale(OP, (1280, 720))

def get_font(size):
    return pygame.font.Font(r"C:\Users\taskm\OneDrive\Desktop\ai game\font.ttf", size)

def easy_mode_quiz():
    questions = [generate_easy_mcq() for _ in range(20)]
    current_q = 0
    selected_option = None
    answered = [False] * 20
    score = 0
    show_hint = False

    while True:
        SCREEN.fill("black")
        mouse_pos = pygame.mouse.get_pos()
        q_data = questions[current_q]
        question = q_data["question"]
        options = q_data["options"]
        correct_answer = q_data["correct_answer"]

        question_render = get_font(32).render(f"Q{current_q + 1}: {question}", True, "White")
        SCREEN.blit(question_render, (100, 100))

        buttons = []
        for i, opt in enumerate(options):
            color = "White"
            if answered[current_q]:
                if opt == correct_answer:
                    color = "Green"
                elif selected_option == opt:
                    color = "Red"
            btn = Button(None, (200, 200 + i * 70), opt, get_font(28), color, "Yellow")
            btn.changeColor(mouse_pos)
            btn.update(SCREEN)
            buttons.append(btn)

        HINT_BUTTON = Button(None, (1000, 100), "Hint", get_font(30), "White", "Orange")
        HINT_BUTTON.changeColor(mouse_pos)
        HINT_BUTTON.update(SCREEN)

        NEXT_BUTTON = Button(None, (1100, 600), "Next", get_font(30), "White", "Green")
        BACK_BUTTON = Button(None, (180, 600), "Back", get_font(30), "White", "Red")

        NEXT_BUTTON.changeColor(mouse_pos)
        BACK_BUTTON.changeColor(mouse_pos)
        NEXT_BUTTON.update(SCREEN)
        BACK_BUTTON.update(SCREEN)

        if show_hint:
            hint_text = get_font(24).render(f"Answer: {correct_answer}", True, "LightBlue")
            SCREEN.blit(hint_text, (800, 150))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not answered[current_q]:
                    for btn in buttons:
                        if btn.checkForInput(mouse_pos):
                            selected_option = btn.text_input
                            answered[current_q] = True
                            if selected_option == correct_answer:
                                score += 1

                if HINT_BUTTON.checkForInput(mouse_pos):
                    show_hint = True

                if NEXT_BUTTON.checkForInput(mouse_pos) and answered[current_q]:
                    if current_q < 19:
                        current_q += 1
                        show_hint = False
                        selected_option = None

                if BACK_BUTTON.checkForInput(mouse_pos) and current_q > 0:
                    current_q -= 1
                    show_hint = False
                    selected_option = None

        if all(answered):
            SCREEN.fill("black")
            result = get_font(50).render(f"You scored {score}/20!", True, "White")
            SCREEN.blit(result, (440, 300))
            home_btn = Button(None, (640, 500), "Return to Menu", get_font(40), "White", "Green")
            home_btn.changeColor(mouse_pos)
            home_btn.update(SCREEN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and home_btn.checkForInput(mouse_pos):
                    main_menu()

        pygame.display.update()

def new_player():
    player_name = ""
    input_box = pygame.Rect(440, 300, 400, 60)
    active = False

    while True:
        SCREEN.fill("black")
        NEW_PLAYER_MOUSE_POS = pygame.mouse.get_pos()

        INSTRUCTIONS = get_font(45).render("Enter Your Gamer Name:", True, "White")
        INSTRUCTIONS_RECT = INSTRUCTIONS.get_rect(center=(640, 200))
        SCREEN.blit(INSTRUCTIONS, INSTRUCTIONS_RECT)

        color = "Green" if active else "White"
        pygame.draw.rect(SCREEN, color, input_box, 2)

        user_text = get_font(45).render(player_name, True, "White")
        SCREEN.blit(user_text, (input_box.x + 10, input_box.y + 10))

        BACK_BUTTON = Button(image=None, pos=(640, 550),
                             text_input="Back", font=get_font(56), base_color="White", hovering_color="Red")
        BACK_BUTTON.changeColor(NEW_PLAYER_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                if BACK_BUTTON.checkForInput(NEW_PLAYER_MOUSE_POS):
                    play()
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN and player_name.strip():
                    difficulty_selection()
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

        pygame.display.update()

def difficulty_selection():
    while True:
        DIFFICULTY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        EASY_BUTTON = Button(image=None, pos=(640, 250), 
                             text_input="Easy", font=get_font(56), base_color="White", hovering_color="Green")
        MEDIUM_BUTTON = Button(image=None, pos=(640, 350), 
                               text_input="Medium", font=get_font(56), base_color="White", hovering_color="Green")
        HARD_BUTTON = Button(image=None, pos=(640, 450), 
                             text_input="Hard", font=get_font(56), base_color="White", hovering_color="Green")
        BACK_BUTTON = Button(image=None, pos=(640, 550), 
                             text_input="Back", font=get_font(56), base_color="White", hovering_color="Red")

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON, BACK_BUTTON]:
            button.changeColor(DIFFICULTY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(DIFFICULTY_MOUSE_POS):
                    easy_mode_quiz()
                if BACK_BUTTON.checkForInput(DIFFICULTY_MOUSE_POS):
                    new_player()

        pygame.display.update()

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        NEW_PLAYER_BUTTON = Button(image=None, pos=(640, 250), 
                                   text_input="New Player", font=get_font(56), base_color="White", hovering_color="Green")
        LOGIN_BUTTON = Button(image=None, pos=(640, 400), 
                              text_input="Log In", font=get_font(56), base_color="White", hovering_color="Green")
        PLAY_BACK = Button(image=None, pos=(640, 550), 
                           text_input="BACK", font=get_font(56), base_color="White", hovering_color="Red")

        for button in [NEW_PLAYER_BUTTON, LOGIN_BUTTON, PLAY_BACK]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEW_PLAYER_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    new_player()
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        GAME_EXPLANATION_BUTTON = Button(image=None, pos=(640, 250), 
                            text_input="Game Explanation", font=get_font(56), base_color="White", hovering_color="Green")
        HISTORY_BUTTON = Button(image=None, pos=(640, 400), 
                            text_input="History", font=get_font(56), base_color="White", hovering_color="Green")
        OPTIONS_BACK = Button(image=None, pos=(640, 550), 
                            text_input="BACK", font=get_font(56), base_color="White", hovering_color="Red")

        for button in [GAME_EXPLANATION_BUTTON, HISTORY_BUTTON, OPTIONS_BACK]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#f01875")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=None, pos=(640, 250), 
                             text_input="PLAY", font=get_font(56), base_color="#d7fcd4", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=None, pos=(640, 400), 
                                text_input="OPTIONS", font=get_font(56), base_color="#d7fcd4", hovering_color="Green")
        QUIT_BUTTON = Button(image=None, pos=(640, 550), 
                             text_input="QUIT", font=get_font(56), base_color="#d7fcd4", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def game_opening_screen():
    while True:
        SCREEN.fill("black")
        SCREEN.blit(OP, (0, 0))

        TITLE_TEXT_1 = get_font(80).render("Game", True, "White")
        TITLE_TEXT_2 = get_font(80).render("Name", True, "White")

        TITLE_RECT_1 = TITLE_TEXT_1.get_rect(center=(1000, 180))
        TITLE_RECT_2 = TITLE_TEXT_2.get_rect(center=(1000, 300))

        SCREEN.blit(TITLE_TEXT_1, TITLE_RECT_1)
        SCREEN.blit(TITLE_TEXT_2, TITLE_RECT_2)

        INSTRUCTIONS = get_font(30).render("Press any key to continue...", True, "White")
        INSTRUCTIONS_RECT = INSTRUCTIONS.get_rect(topright=(1250, 620))
        SCREEN.blit(INSTRUCTIONS, INSTRUCTIONS_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                main_menu()

        pygame.display.update()

game_opening_screen()
