class GridPlayer:

    def __init__(self):
        self.foo = True

    def tick(self, game_map, your_units, enemy_units, resources, turns_left):
        return []

        # Meele can only beat on opps directly adjacent to them
        # It would be a good idea to use an A* search for their decisions

        # Worker units can mine new resources from the blocks
        # They should seek these out as optimally as they can
        # Probably some sort of uniform search, keeping in mind the danger of opps

        # As our number of current players changes, it might also be a better idea
        # to shift our meele's priority from protecting workers to aggression towards ops

        # Zerg rush would let us go for the opponent's guys

        for worker in your_units.get_all_unit_of_type('worker'):
            # Greedy search for resource blocks
            # Favor blocks farther away from ops

           
            # None in our case means to stay still
            closest_resource_dir = "NONE"

            level = 0 # As this increases, more spots to search
            
            cur_x, cur_y = worker.position()

            if level == 0:

                # We can't move diagonal...
                for x, y in [ (cur_x, cur_y + 1), #DOWN
                              (cur_x - 1, cur_y), #LEFT
                              (cur_x + 1, cur_y), #RIGHT 
                              (cur_x, cur_y - 1)  #UP
                            ]: #Keep in mind we can also stay in current spot

                    # Take initial snapshot of the battlefield
                    # Hardcode values of resources initially




        for melee in your_units.get_all_unit_of_type('melee'):
            # Zerg rush
            # May need to also consider protection on our own guys



