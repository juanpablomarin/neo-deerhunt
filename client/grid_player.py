import random
from helper_classes import *

class GridPlayer:

    def __init__(self):
        self.foo = True

    def tick(self, game_map, your_units, enemy_units, resources, turns_left):
        
        moves = []

        # Meele can only beat on opps directly adjacent to them
        # It would be a good idea to use an A* search for their decisions

        # Worker units can mine new resources from the blocks
        # They should seek these out as optimally as they can
        # Probably some sort of uniform search, keeping in mind the danger of opps

        # As our number of current players changes, it might also be a better idea
        # to shift our meele's priority from protecting workers to aggression towards ops

        # Zerg rush would let us go for the opponent's guys

        current_pos_mappings = {}
        intention_mappings   = {}

        for unit in your_units.get_all_unit_ids():
            current_pos_mappings[unit.position] = unit

        # Now I know where all my players are located before any of them move

        for worker in your_units.get_all_unit_of_type('worker'):
            # Greedy search for resource blocks
            # Favor blocks farther away from ops

           
            # None in our case means to stay still
            #closest_resource_dir = "NONE"

            #level = 0 # As this increases, more spots to search
            
            #cur_x, cur_y = worker.position()

            # Copy the items in the grid without the object itself -- can't call the method
            temp_map = game_map.grid

            # THERE are issues here...
            closest_res = game_map.closest_resources(worker)

            if closest_res in intention_mappings:
                # If I have a teammate going there, I don't want to also go there
                # Thats kinda hard, so lets just consider when we ALREADY have a teammate there
                while closest_res in intention_mappings:
                    
                    temp_map[closest_res[0]] = ""
                    temp_map = Map(temp_map)

                    closest_res = temp_map.closest_resources(worker.position)
                    temp_map = temp_map.grid

            else:
                intention_mappings[closest_res] = worker



            path = game_map.bfs(worker.position(), closest_res)

            # Issue with this is that all workers are going to go to the same 
            # resource
            moves.append(worker.move(path[0]))


        for melee in your_units.get_all_unit_of_type('melee'):
            # Zerg rush
            # May need to also consider protection on our own guys
            dirs = ["LEFT", "RIGHT", "UP", "DOWN"]

            moves.append(melee.move(dirs[random.randint(0, 4)]))


