# Score and Timer
# Track a score counter and a countdown timer.
# Run this in the MakeCode Arcade Python editor at https://arcade.makecode.com/

info.setScore(0)
info.startCountdown(30)

hero = sprites.create(img"""
    . . . . . . . . . . . . . . . .
    . . . . . 5 5 5 5 5 . . . . . .
    . . . . 5 5 5 5 5 5 5 . . . . .
    . . . . . 5 5 5 5 5 . . . . . .
    . . . . . . . . . . . . . . . .
""", SpriteKind.player)

controller.moveSprite(hero)

def on_A_pressed():
    info.changeScoreBy(1)

controller.A.onEvent(ControllerButtonEvent.Pressed, on_A_pressed)
