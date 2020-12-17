let i: number;
let atone = 0
scene.setBackgroundColor(7)
let s_image = img`
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
`
let my_is = [s_image]
let my_sprite = sprites.create(img`
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
`, SpriteKind.Player)
//  other is enemy
let other_sprite = sprites.create(img`
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
`, SpriteKind.Enemy)
let my_sprites = [my_sprite, other_sprite]
let start_y = 0
let start_x = 200
let str = `    
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
    4 4 4 4 . . . . . . . . . . . . `
my_is[0] = img`
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
`
my_is[1] = my_is[0].clone()
my_is[1].flipY()
for (i = 0; i < 80; i++) {
    if (i % 10 == 0) {
        start_y += 25
        start_x = start_x - 190
    }
    
    start_x += 20
    if (i % 2 == 0) {
        my_sprites[i] = sprites.create(my_is[0])
    } else {
        my_sprites[i] = sprites.create(my_is[1])
    }
    
    // s_image.fill(5)
    my_sprites[i].setPosition(start_x, start_y)
}
// if (i == 5):
//     my_sprites[i].set_flag(SpriteFlag.StayInScreen, True)
other_sprite.follow(my_sprite, 40, 100)
other_sprite.setPosition(5, 5)
other_sprite.setFlag(SpriteFlag.StayInScreen, true)
my_sprite.setVelocity(50, 50)
controller.moveSprite(my_sprite)
scene.cameraFollowSprite(my_sprite)
game.onUpdateInterval(500, function on_update() {
    
    let tones = [440, 525, 590]
    atone = (atone + 1) % 3
    // randint(0,2)
    music.ringTone(tones[atone])
    my_is[1].flipX()
    my_is[0].flipY()
    let ok = false
    for (let i = 0; i < 80; i++) {
        if (my_sprites[i].overlapsWith(my_sprite)) {
            ok = true
        }
        
    }
    if (ok == false) {
        game.over()
    }
    
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_overlap(sprite: Sprite, otherSprite: Sprite) {
    scene.cameraShake()
    game.over()
})
