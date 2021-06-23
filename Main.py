import arcade



SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "game"

CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5

class gameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.AQUA)

        self.coin_list = None 
        self.wall_list = None 
        self.player_list = None 
        self.player_sprite = None 

    
        

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)
        image_source = "adventurer_kick.png"
        self.player_sprite = arcade.Sprite(image_source)
        self.player_sprite.center_x = SCREEN_WIDTH/2
        self.player_sprite.center_y = SCREEN_HEIGHT/2
        self.player_list.append(self.player_sprite)

        self.player_sprite.speed = 10
        self.player_sprite.right = False
        self.player_sprite.left = False
        self.player_sprite.up = False
        self.player_sprite.down = False

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.wall_list.draw()
        self.player_list.draw()
    
    def update(self, delta_time):
        self.player_sprite.update()



    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.player_sprite.change_x = self.player_sprite.speed
        if symbol == arcade.key.LEFT:
            self.player_sprite.change_x = -self.player_sprite.speed
        if symbol == arcade.key.UP:
             self.player_sprite.change_y = -self.player_sprite.speed
        if symbol == arcade.key.DOWN:
             self.player_sprite.change_y = self.player_sprite.speed



def main():
    window = gameWindow()
    window.setup()
    arcade.run()

main()





