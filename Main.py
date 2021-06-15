import arcade



SCREN_WIDTH = 600
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

def on_draw(self):
    arcade.start_render()

def main():
    window = gameWindow()
    window.setup()
    arcade.run()





