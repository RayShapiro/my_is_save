atone = 0
scene.set_background_color(7)

s_image = myTiles.transparency16
my_is = [s_image]

# create sprites
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

tiles.set_tilemap(tilemap("""level"""))

# images for tilemap
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

# layout tiles programatically
start_x = 0
start_y = 0
for i in range(200):
    if (i%20 == 0):
        start_y += 1
        start_x = i/40

    start_x += 1

    loc = tiles.get_tile_location(start_x, start_y)
    tiles.set_tile_at(loc, my_is[i%2])


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

def on_overlap_tile(sprite, location):
    game.over()

scene.on_overlap_tile(SpriteKind.player, s_image, on_overlap_tile)
    
