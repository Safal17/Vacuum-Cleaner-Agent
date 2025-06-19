# utility_agent.py
from environment import VacuumEnvironment
import math


class UtilityVacuumAgent:
    def __init__(self, env):
        self.env = env
        self.visited = [[0 for _ in range(env.width)] for _ in range(env.height)]

    def act(self):
        x, y = self.env.agent_pos

        # Increase visit count for current cell
        self.visited[y][x] += 1

        # Check current cell
        if self.env.is_dirty(x, y):
            self.env.clean_cell(x, y)
            print(f"Cleaned cell ({x}, {y})")
            return

        # Calculate utility for all possible moves
        possible_moves = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1), (0, 1),
                          (1, -1), (1, 0), (1, 1)]

        best_utility = -float('inf')
        best_move = (0, 0)

        for dx, dy in possible_moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.env.width and 0 <= ny < self.env.height:
                utility = self.calculate_utility(nx, ny)
                if utility > best_utility:
                    best_utility = utility
                    best_move = (dx, dy)

        # Execute the best move
        self.env.move_agent(best_move[0], best_move[1])
        print(f"Moved to ({self.env.agent_pos[0]}, {self.env.agent_pos[1]})")

    def calculate_utility(self, x, y):
        # Utility is higher for dirty cells
        dirt_utility = 10 if self.env.is_dirty(x, y) else 0

        # Utility decreases with visit count (to encourage exploration)
        visit_penalty = -2 * self.visited[y][x]

        # Utility decreases with distance from current position (to encourage efficiency)
        current_x, current_y = self.env.agent_pos
        distance = math.sqrt((x - current_x) ** 2 + (y - current_y) ** 2)
        distance_penalty = -distance

        return dirt_utility + visit_penalty + distance_penalty


def run_utility_agent():
    env = VacuumEnvironment(width=5, height=5, dirt_prob=0.3)
    agent = UtilityVacuumAgent(env)

    print("Initial Environment:")
    env.print_env()

    steps = 0
    max_steps = 100

    while not env.goal_test() and steps < max_steps:
        print(f"\nStep {steps + 1}:")
        agent.act()
        env.print_env()
        steps += 1

    if env.goal_test():
        print(f"Room cleaned in {steps} steps!")
    else:
        print(f"Stopped after {max_steps} steps without cleaning all cells.")


if __name__ == "__main__":
    run_utility_agent()
