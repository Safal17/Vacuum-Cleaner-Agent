# goal_based_agent.py
from environment import VacuumEnvironment
from collections import deque


class GoalBasedVacuumAgent:
    def __init__(self, env):
        self.env = env
        self.memory = [[False for _ in range(env.width)] for _ in range(env.height)]
        self.path = []

    def act(self):
        x, y = self.env.agent_pos

        # Mark current position as visited
        self.memory[y][x] = True

        # Check current cell
        if self.env.is_dirty(x, y):
            self.env.clean_cell(x, y)
            print(f"Cleaned cell ({x}, {y})")
            return

        # If we have a path, follow it
        if self.path:
            next_pos = self.path.pop(0)
            dx = next_pos[0] - x
            dy = next_pos[1] - y
            self.env.move_agent(dx, dy)
            print(f"Moved to ({self.env.agent_pos[0]}, {self.env.agent_pos[1]})")
            return

        # Find nearest unvisited dirty cell using BFS
        target = self.find_nearest_dirty()
        if target:
            self.path = self.find_path((x, y), target)
            if self.path:
                next_pos = self.path.pop(0)
                dx = next_pos[0] - x
                dy = next_pos[1] - y
                self.env.move_agent(dx, dy)
                print(f"Moved to ({self.env.agent_pos[0]}, {self.env.agent_pos[1]})")
            return

        # If no dirty cells found but environment isn't clean, explore unvisited cells
        target = self.find_nearest_unvisited()
        if target:
            self.path = self.find_path((x, y), target)
            if self.path:
                next_pos = self.path.pop(0)
                dx = next_pos[0] - x
                dy = next_pos[1] - y
                self.env.move_agent(dx, dy)
                print(f"Moved to ({self.env.agent_pos[0]}, {self.env.agent_pos[1]})")

    def find_nearest_dirty(self):
        # BFS to find nearest dirty cell
        x, y = self.env.agent_pos
        visited = [[False for _ in range(self.env.width)] for _ in range(self.env.height)]
        queue = deque([(x, y, [])])
        visited[y][x] = True

        possible_moves = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1), (0, 1),
                          (1, -1), (1, 0), (1, 1)]

        while queue:
            cx, cy, path = queue.popleft()

            if self.env.is_dirty(cx, cy):
                return (cx, cy)

            for dx, dy in possible_moves:
                nx, ny = cx + dx, cy + dy
                if (0 <= nx < self.env.width and 0 <= ny < self.env.height and
                        not visited[ny][nx]):
                    visited[ny][nx] = True
                    new_path = path + [(nx, ny)]
                    queue.append((nx, ny, new_path))

        return None

    def find_nearest_unvisited(self):
        # BFS to find nearest unvisited cell
        x, y = self.env.agent_pos
        visited = [[False for _ in range(self.env.width)] for _ in range(self.env.height)]
        queue = deque([(x, y, [])])
        visited[y][x] = True

        possible_moves = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1), (0, 1),
                          (1, -1), (1, 0), (1, 1)]

        while queue:
            cx, cy, path = queue.popleft()

            if not self.memory[cy][cx]:
                return (cx, cy)

            for dx, dy in possible_moves:
                nx, ny = cx + dx, cy + dy
                if (0 <= nx < self.env.width and 0 <= ny < self.env.height and
                        not visited[ny][nx]):
                    visited[ny][nx] = True
                    new_path = path + [(nx, ny)]
                    queue.append((nx, ny, new_path))

        return None

    def find_path(self, start, end):
        # BFS to find path from start to end
        sx, sy = start
        ex, ey = end
        visited = [[False for _ in range(self.env.width)] for _ in range(self.env.height)]
        queue = deque([(sx, sy, [])])
        visited[sy][sx] = True

        possible_moves = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1), (0, 1),
                          (1, -1), (1, 0), (1, 1)]

        while queue:
            cx, cy, path = queue.popleft()

            if (cx, cy) == (ex, ey):
                return path

            for dx, dy in possible_moves:
                nx, ny = cx + dx, cy + dy
                if (0 <= nx < self.env.width and 0 <= ny < self.env.height and
                        not visited[ny][nx]):
                    visited[ny][nx] = True
                    new_path = path + [(nx, ny)]
                    queue.append((nx, ny, new_path))

        return []


def run_goal_based_agent():
    env = VacuumEnvironment(width=5, height=5, dirt_prob=0.3)
    agent = GoalBasedVacuumAgent(env)

    print("Initial Environment:")
    env.print_env()

    steps = 0
    max_steps = 200

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
    run_goal_based_agent()
