def jogo():

    pygame.init()
    pygame.mixer.init()
    score=0
    pygame.mixer.music.play(loops=-1)
    while True:
        pygame.time.Clock().tick(15)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                    snake_direction = event.key


        screen.blit(apple_surface, apple_pos)

        if collision(apple_pos, snake_pos[0]):
            mordendo_sound.play()
            snake_pos.append((-10, -10))
            apple_pos = random_on_grid()
            score+=10
            print(score)

        for pos in snake_pos:
            screen.blit(snake_surface, pos)

        for i in range(len(snake_pos) - 1, 0, -1):
            if collision(snake_pos[0], snake_pos[i]):
                #restart_game()
                pygame.quit()
                quit()
                break
            snake_pos[i] = snake_pos[i - 1]

        if off_limits(snake_pos[0]):
        
        pygame.quit()
        quit()

        if snake_direction == K_UP:
            snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)
        elif snake_direction == K_DOWN:
            snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)
        elif snake_direction == K_LEFT:
            snake_pos[0] = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])
        elif snake_direction == K_RIGHT:
            snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])