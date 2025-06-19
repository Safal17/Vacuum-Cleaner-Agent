# Vacuum-Cleaner-Agent

## Project Overview
This project implements three types of intelligent agents for vacuum cleaning:
1. **Reflex Agent** - Reacts only to current percepts
2. **Goal-Based Agent** - Uses memory and pathfinding
3. **Utility-Based Agent** - Makes decisions based on calculated utilities

## Theoretical Background

### Agent Types Explained

**1. Reflex Agent**
- Simple stimulus-response behavior
- Cleans current cell if dirty
- Moves randomly when current cell is clean
- No memory or long-term planning

**2. Goal-Based Agent**
- Maintains internal state/memory
- Uses BFS to find nearest dirty cell
- Plans optimal paths to target locations
- More efficient than reflex agent

**3. Utility-Based Agent**
- Assigns numerical values to possible actions
- Considers:
  - Dirt proximity (higher utility for dirty cells)
  - Visit frequency (avoids revisiting clean cells)
  - Movement cost (prefers closer cells)
- Balances exploration vs exploitation

## Environment Representation
- Grid world with random dirt distribution
- '1' represents dirty cells
- '0' represents clean cells
- 'A' marks the agent's position

## How to Run
```bash
# Run each agent type
python reflex_agent.py
python goal_based_agent.py
python utility_agent.py
