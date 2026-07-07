# Tilemap Walk
# Walk a sprite through a simple tilemap with wall collision.
# Run this in the MakeCode Arcade Python editor at https://arcade.makecode.com/

scene.setTileMap(tilemap"""
    level1
""")

hero = sprites.create(img"""
    . . . . . . . . . . . . . . . .
    . . . . . 5 5 5 5 5 . . . . . .
    . . . . 5 5 5 5 5 5 5 . . . . .
    . . . . . 5 5 5 5 5 . . . . . .
    . . . . . . . . . . . . . . . .
""", SpriteKind.player)

scene.placeOnRandomTile(hero, assets.tile("""myTile"""))
controller.moveSprite(hero)
scene.cameraFollowSprite(hero)
