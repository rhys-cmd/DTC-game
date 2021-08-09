import arcade


GRAVITY = 1
PLAYER_JUMP_SPEED = 10



SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
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
        self.jump_sound = arcade.load_sound("BeepBox-Song.mp3")

        self.view_bottom = 0
        self.view_left = 0


        

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)
        image_source = "ghost-1.png (1).png"
        self.player_sprite = arcade.Sprite(image_source)
        self.player_sprite.center_x = SCREEN_WIDTH/2
        self.player_sprite.center_y = SCREEN_HEIGHT/2
        self.player_list.append(self.player_sprite)

        self.player_sprite.speed = 5
        self.player_sprite.right = False
        self.player_sprite.left = False
        self.player_sprite.up = False
        self.player_sprite.down = False

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)
        # Put some crates on the ground
        # This shows using a coordinate list to place sprites
        coordinate_list = [[512, 96],
                            [256, 96],
                            [768, 96]]
        
        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)
    
    self.physics_engine.update
    
    changed = False

    #scroll left
    left_boundary = self.view_left + SCREEN_WIDTH - LEFT_VIEWPORT_MARGIN
    if self.player_sprite.right > right_boundary:
        self.view_left -= left_boundary - right_boundary
        changed = True

    #scroll right
    right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
    if self.player_sprite.right > right_boundary:
        self.view_left -= left_boundary - right_boundary
        changed = True

    #scroll up
    top_boundary = slef.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
    if self.player_sprite.top > top_boundary:
        self.view_bottom += self.player_sprite.top - top - top_boundary
        changed  = True


    #scroll down
    bottom_boundary = self.veiw_bottom + BOTTOM_VIEWPORT_MARGIN
    if self.player_sprite.bottom < bottom_boundary:
        self.veiw_bottom -= bottom_boundary - self.player_sprite.bottom
        changed = True


    if changed:
        self.veiw_bottom = int(self.veiw_bottom)
        self.veiw_left = int(self.veiw_left)
    
    
    arcade.set_viewport(self.veiw_left,
                    SCREEN_WIDTH + self.veiw_left,
                    self.view_bottom,
                    SCREEN_HEIGHT + self.veiw_bottom )

    LEFT_VIEWPORT_MARGIN = 250
    RIGHT_VIEWPORT_MARGIN = 250
    BOTTOM_VIEWPORT_MARGIN = 250
    TOP_VIEWPORT_MARGIN = 100
    
    
    
    
    
    
    
    
    
    
    
    
    
    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.wall_list.draw()
        self.player_list.draw()
    
    def update(self, delta_time):
        self.player_sprite.update()
        self.physics_engine.update()


    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            if self.physics_engine.can_jump(): 
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        if symbol == arcade.key.LEFT:
            self.player_sprite.change_x = -self.player_sprite.speed
        if symbol == arcade.key.DOWN:
             self.player_sprite.change_y = -self.player_sprite.speed
        if symbol == arcade.key.RIGHT:
             self.player_sprite.change_x = self.player_sprite.speed

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT: 
            self.player_sprite.change_x = 0
        if symbol == arcade.key.LEFT: 
            self.player_sprite.change_x = 0 
        if symbol == arcade.key.UP: 
            self.player_sprite.change_y = 0 
        if symbol == arcade.key.DOWN: 
            self.player_sprite.change_y = 0  

    




def main():
    window = gameWindow()
    window.setup()
    arcade.run()

main()





