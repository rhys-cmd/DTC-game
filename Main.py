import arcade


GRAVITY = 0.4
PLAYER_JUMP_SPEED = 7



SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "game"


CHARACTER_SCALING = 1

LEFT_VIEW_PORT_MARGIN = 400
RIGHT_VIEW_PORT_MARGIN = 400
BOTTOM_VIEW_PORT_MARGIN = 100
TOP_VIEW_PORT_MARGIN = 200

TILE_SCALING = 1.5
COIN_SCALING = 2

PLAYER_START_Y = 100
PLAYER_START_X = 100






class gameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.AQUA)
        
        
        self.coin_list = None 
        self.wall_list = None 
        self.player_list = None 
        self.player_sprite = None 
        self.jump_sound = arcade.load_sound("BeepBox-Song.mp3")
        self.dont_touch_layer = None
        self.touch_to_win_list = None
        
        
        self.view_bottom = 0
        self.view_left = 0
        
        self.score = 3
        self.level = 1
        
        self.tile_map = None
        

    def setup(self, level):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)
        image_source = "ghost-1.png (1).png"
        self.player_sprite = arcade.Sprite(image_source)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.player_list.append(self.player_sprite)
        self.camera = arcade.Camera(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.gui_camera = arcade.Camera(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

       

        self.player_sprite.speed = 3
        self.player_sprite.right = False
        self.player_sprite.left = False
        self.player_sprite.up = False
        self.player_sprite.down = False
        
        

        self.score = 3

        platform_layer_name = "Tile Layer 1"
        dont_touch_layer = "Tile Layer 2"
        touch_to_win_layer = "Tile Layer 3"
    
    
        map_name = f"dtctilemap_{level}.tmx"

        
        

        my_map =  arcade.tilemap.read_tmx(map_name)
        self.wall_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=platform_layer_name,
                                                      scaling=TILE_SCALING,
                                                      use_spatial_hash=True)
        
        my_map =  arcade.tilemap.read_tmx(map_name)
        self.dont_touch_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=dont_touch_layer,
                                                      scaling=TILE_SCALING,
                                                      use_spatial_hash=True)

        my_map = arcade.tilemap.read_tmx(map_name)
        self.touch_to_win_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=touch_to_win_layer,
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
        self.touch_to_win_list.draw()
        self.dont_touch_list.draw()
        
        control_text = f"use arrow keys to move"
        arcade.draw_text(control_text,
                10,
                10,
                arcade.csscolor.WHITE,
                18)
        
        

           
        score_text = f"Score: {self.score}"
        arcade.draw_text(
                score_text,
                10,
                10,
                arcade.csscolor.WHITE,
                18,
        )
    
    
    def on_update(self, delta_time):
        self.player_sprite.update()
        self.physics_engine.update()
        
        changed = False


        
            

        if self.player_sprite.center_y < -500:
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y
            self.score - 1

            self.view_bottom = 0
            self.view_left = 0
            self.score -= 1
            changed = True




        if arcade.check_for_collision_with_list(self.player_sprite,
                                            self.dont_touch_list):
            self.player_sprite.center_y = PLAYER_START_Y
            self.player_sprite.center_x = PLAYER_START_X
            self.view_bottom = 0
            self.view_left = 0
            self.score -= 1
            changed = True


        if arcade.check_for_collision_with_list(self.player_sprite,
                                                self.touch_to_win_list):
            self.level += 1
            self.setup(self.level)                    
            
            self.view_bottom = 0
            self.view_left = 0
            changed = True

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
        if symbol == arcade.key.DOWN: 
            self.player_sprite.change_y = 0  




    



def main():
    window = gameWindow()
    window.setup(window.level)
    arcade.run()

main()





