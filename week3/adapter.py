class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        h = len(grid)
        w = len(grid[0])
        self.adaptee.set_dim((w, h))
        lights, obstacles = [], []

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    lights.append((j, i))
                elif cell == -1:
                    obstacles.append((j, i))
        
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)

        return self.adaptee.generate_lights()
