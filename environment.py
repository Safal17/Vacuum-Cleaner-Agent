# environment.py
import random


class VacuumEnvironment:
    def __init__(self, width=5, height=5, dirt_prob=0.2):
        self.width = width
        self.height = height
        self.grid = [[1 if random.random() < dirt_prob else 0 for _ in range(width)] for _ in range(height)]
        self.agent_pos = (random.randint(0, width - 1), random.randint(0, height - 1))

    def is_dirty(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x] == 1
        return False

    def clean_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 0

    def move_agent(self, dx, dy):
        new_x = self.agent_pos[0] + dx
        new_y = self.agent_pos[1] + dy
        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            self.agent_pos = (new_x, new_y)

    def goal_test(self):
        return all(cell == 0 for row in self.grid for cell in row)

    def print_env(self):
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if (x, y) == self.agent_pos:
                    row.append('A')
                else:
                    row.append(str(self.grid[y][x]))
            print(' '.join(row))
        print()

if __name__ == "__main__":
    env = VacuumEnvironment(width=5, height=5, dirt_prob=0.2)
    print("Initial Environment:")
    env.print_env()