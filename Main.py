import arcade

GRAVITY = 1
PLAYER_JUMP_SPEED = 10



SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "game"

CHARACTER_SCALING = 1

LEFT_VIEW_PORT_MARGIN = 250
RIGHT_VIEW_PORT_MARGIN = 250
BOTTOM_VIEW_PORT_MARGIN = 50
TOP_VIEW_PORT_MARGIN = 100

TILE_SCALING = 1
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


        self.tile_map = None

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
 
        
        
        map_name = "dtctilemap1.tmx"
        platform_layer_name = "Tile Layer 1"

        my_map =  arcade.tilemap.read_tmx(map_name)
        self.wall_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=platform_layer_name,
                                                      scaling=TILE_SCALING,
                                                      use_spatial_hash=True)
        
        
    

        
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)
    
        self.physics_engine.update
    
     
    changed = False

   

   
    
    
    
    
    
    
    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.wall_list.draw()
        self.player_list.draw()
    
    
    def on_update(self, delta_time):
        self.player_sprite.update()
        self.physics_engine.update()

        changed = False

        left_boundary = self.view_left + LEFT_VIEW_PORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEW_PORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True
       
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEW_PORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True
        
        bottom_boundary = self.view_bottom + BOTTOM_VIEW_PORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


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





