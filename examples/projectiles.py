# Projectiles
# Shoot a projectile from the player sprite when the A button is pressed.
# Run this in the MakeCode Arcade Python editor at https://arcade.makecode.com/

hero = sprites.create(img"""
    . . . . . . . . . . . . . . . .
    . . . . . 5 5 5 5 5 . . . . . .
    . . . . 5 5 5 5 5 5 5 . . . . .
    . . . . . 5 5 5 5 5 . . . . . .
    . . . . . . . . . . . . . . . .
""", SpriteKind.player)

controller.moveSprite(hero)

def on_A_pressed():
    projectile = sprites.createProjectileFromSprite(img"""
        . 2 .
        2 2 2
        . 2 .
    """, hero, 80, 0)
    projectile.setKind(SpriteKind.projectile)

controller.A.onEvent(ControllerButtonEvent.Pressed, on_A_pressed)

sprites.onOverlap(SpriteKind.projectile, SpriteKind.enemy, lambda s, e: (
    s.destroy(),
    e.destroy(),
    info.changeScoreBy(1)
))
