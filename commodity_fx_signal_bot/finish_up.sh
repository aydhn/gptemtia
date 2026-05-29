#!/bin/bash
set -e
git add .
git commit -m "feat: Add controlled offline scenario and synthetic demonstration capabilities

- Introduce ScenarioProfile and ScenarioRegistry.
- Implement sample data builder for synthetic OHLCV.
- Implement fixture, workflow pack, and expected output generators.
- Create scenario dry-run executor.
- Add scenario CLI scripts.
- Update docs."
