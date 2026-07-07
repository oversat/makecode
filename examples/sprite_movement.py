# Sprite Movement
# Move a sprite with the directional pad (d-pad).
# Run this in the MakeCode Arcade Python editor at https://arcade.makecode.com/

hero = sprites.create(img"""
    . . . . . . . . . . . . . . . .
    . . . . . 5 5 5 5 5 . . . . . .
    . . . . 5 5 5 5 5 5 5 . . . . .
    . . . 5 5 5 5 5 5 5 5 5 . . . .
    . . . 5 5 5 5 5 5 5 5 5 . . . .
    . . . . 5 5 5 5 5 5 5 . . . . .
    . . . . . 5 5 5 5 5 . . . . . .
    . . . . . . . . . . . . . . . .
""", SpriteKind.player)

controller.moveSprite(hero)
scene.cameraFollowSprite(hero)
