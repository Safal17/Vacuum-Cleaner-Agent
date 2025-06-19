# reflex_agent.py
from environment import VacuumEnvironment
import random


class ReflexVacuumAgent:
    def __init__(self, env):
        self.env = env

    def act(self):
        x, y = self.env.agent_pos

        # Check current cell
        if self.env.is_dirty(x, y):
            self.env.clean_cell(x, y)
            print(f"Cleaned cell ({x}, {y})")
            return

        # If current cell is clean, move to a random adjacent cell
        possible_moves = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1), (0, 1),
                          (1, -1), (1, 0), (1, 1)]

        # Filter valid moves
        valid_moves = []
        for dx, dy in possible_moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.env.width and 0 <= new_y < self.env.height:
                valid_moves.append((dx, dy))

        if valid_moves:
            dx, dy = random.choice(valid_moves)
            self.env.move_agent(dx, dy)
            print(f"Moved to ({self.env.agent_pos[0]}, {self.env.agent_pos[1]})")


def run_reflex_agent():
    env = VacuumEnvironment(width=5, height=5, dirt_prob=0.3)
    agent = ReflexVacuumAgent(env)

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
    run_reflex_agent()
