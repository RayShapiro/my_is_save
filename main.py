atone = 0
scene.set_background_color(7)

s_image = img("""
    . . . . . . . . . . . . . . . .
    . 2 2 2 2 . . . 3 3 3 3 3 3 3 .
    . 2 2 2 2 . . . . . . . . . 3 .
    . 2 2 2 2 . . . . . . . . . 3 .
    . . . . . . . . . . . . . . 3 .
    . . . . . . . . . . . . . . 3 .
    . . . . 5 5 5 5 . . . . . . 3 .
    . . . . 5 5 5 5 . . . . . . 3 .
    . . . . 5 5 5 5 . . . . . . 3 .
    . . . . . . . . . . . . . . 3 .
    . . . . . . . . . . . . . . 3 .
    . . . . . . . . 8 8 8 8 . . 3 .
    . . . . . . . . 8 8 8 8 . . . .
    . . . . . . . . 8 8 8 8 . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
""")
my_is = [s_image]

my_sprite = sprites.create(img("""
    . . . . . . f f f f . . . . . .
    . . . . f f f 2 2 f f f . . . .
    . . . f f f 2 2 2 2 f f f . . .
    . . f f f e e e e e e f f f . .
    . . f f e 2 2 2 2 2 2 e e f . .
    . . f e 2 f f f f f f 2 e f . .
    . . f f f f e e e e f f f f . .
    . f f e f b f 4 4 f b f e f f .
    . f e e 4 1 f d d f 1 4 e e f .
    . . f e e d d d d d d e e f . .
    . . . f e e 4 4 4 4 e e f . . .
    . . e 4 f 2 2 2 2 2 2 f 4 e . .
    . . 4 d f 2 2 2 2 2 2 f d 4 . .
    . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
    . . . . . f f f f f f . . . . .
    . . . . . f f . . f f . . . . .
"""), SpriteKind.player)

# other is enemy
other_sprite = sprites.create(img("""
    . . . . . . b b b b . . . . . .
    . . . . . . b 4 4 4 b . . . . .
    . . . . . . b b 4 4 4 b . . . .
    . . . . . b 4 b b b 4 4 b . . .
    . . . . b d 5 5 5 4 b 4 4 b . .
    . . . . b 3 2 3 5 5 4 e 4 4 b .
    . . . b d 2 2 2 5 7 5 4 e 4 4 e
    . . . b 5 3 2 3 5 5 5 5 e e e e
    . . b d 7 5 5 5 3 2 3 5 5 e e e
    . . b 5 5 5 5 5 2 2 2 5 5 d e e
    . b 3 2 3 5 7 5 3 2 3 5 d d e 4
    . b 2 2 2 5 5 5 5 5 5 d d e 4 .
    b d 3 2 d 5 5 5 d d d 4 4 . . .
    b 5 5 5 5 d d 4 4 4 4 . . . . .
    4 d d d 4 4 4 . . . . . . . . .
    4 4 4 4 . . . . . . . . . . . .
"""), SpriteKind.enemy)
my_sprites = [my_sprite, other_sprite]
start_y = 0
start_x = 200

str = """    
    . . . . . . b b b b . . . . . .
    . . . . . . b 4 4 4 b . . . . .
    . . . . . . b b 4 4 4 b . . . .
    . . . . . b 4 b b b 4 4 b . . .
    . . . . b d 5 5 5 4 b 4 4 b . .
    . . . . b 3 2 3 5 5 4 e 4 4 b .
    . . . b d 2 2 2 5 7 5 4 e 4 4 e
    . . . b 5 3 2 3 5 5 5 5 e e e e
    . . b d 7 5 5 5 3 2 3 5 5 e e e
    . . b 5 5 5 5 5 2 2 2 5 5 d e e
    . b 3 2 3 5 7 5 3 2 3 5 d d e 4
    . b 2 2 2 5 5 5 5 5 5 d d e 4 .
    b d 3 2 d 5 5 5 d d d 4 4 . . .
    b 5 5 5 5 d d 4 4 4 4 . . . . .
    4 d d d 4 4 4 . . . . . . . . .
    4 4 4 4 . . . . . . . . . . . . """


my_is[0]=img("""
    . . . . . . . . . . . . . . . .
    . 2 2 2 2 . . . 3 3 3 3 3 3 3 .
    . 2 2 2 2 . . . . . . . . . 3 .
    . 2 2 2 2 . . . . . . . . . 3 .
    . . . . . . . . . . . . . . 3 .
    . . . . . . . . . . . . . . 3 .
    . . . . 5 5 5 5 . . . . . . 3 .
    . . . . 5 5 5 5 . . . . . . 3 .
    . . . . 5 5 5 5 . . . . . . 3 .
    . . . . . . . . . . . . . . 3 .
    . . . . . . . . . . . . . . 3 .
    . . . . . . . . 8 8 8 8 . . 3 .
    . . . . . . . . 8 8 8 8 . . . .
    . . . . . . . . 8 8 8 8 . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
""")

my_is[1] = my_is[0].clone()
my_is[1].flip_y()

for i in range(0, 80):
    if (i%10 == 0):
        start_y += 25
        start_x = start_x - 190

    start_x += 20

    if (i%2 == 0):
        my_sprites[i] = sprites.create(my_is[0])
    else:
        my_sprites[i] = sprites.create(my_is[1])
    #s_image.fill(5)

    my_sprites[i].set_position(start_x, start_y)
    #if (i == 5):
    #    my_sprites[i].set_flag(SpriteFlag.StayInScreen, True)

other_sprite.follow(my_sprite, 40, 100)
other_sprite.set_position(5, 5)
other_sprite.set_flag(SpriteFlag.StayInScreen, True)

my_sprite.set_velocity(50, 50)
controller.move_sprite(my_sprite)
scene.camera_follow_sprite(my_sprite)
game.on_update_interval(500, on_update)
def on_overlap(sprite, otherSprite):
    scene.camera_shake()
    game.over()

sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap)

def on_update():
    global atone
    tones = [440, 525, 590]
    atone = (atone +1 ) %3 #randint(0,2)
    music.ring_tone(tones[atone])
    my_is[1].flip_x()
    my_is[0].flip_y()

    ok = False
    for i in range(80):
        if my_sprites[i].overlaps_with(my_sprite):
            ok = True

    if (ok == False):
        game.over()
    #x = my_sprite.
    #if (x > 10):
        #    music.stop_all_sounds()
    #for im in my_is:
        #    im.flip_y()my_sprite.overlaps_with(None)