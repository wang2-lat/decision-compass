# Decision Compass

A CLI tool to help founders make critical decisions with clarity and confidence.

## Features

- **Decision Framework**: Structured questionnaires for quit-job, cofounder, and project decisions
- **Risk/Reward Scoring**: Multi-dimensional scoring system to quantify decision factors
- **Decision Log**: Track your decision history and review past choices

## Installation


## Usage

### Make a new decision


### View decision history


### Review a specific decision


## Decision Types

- **quit-job**: Should you quit your job to work on your startup full-time?
- **cofounder**: Should you partner with this person as a cofounder?
- **project**: Should you continue or pivot your current project?

## How It Works

1. Answer 7 questions on a scale of 1-10
2. Get risk, reward, timing, and confidence scores
3. Receive a data-driven recommendation
4. Record your final decision for future reference

## Data Storage

Decisions are stored locally in `~/.decision_compass.json`
pip install -r requirements.txt
python main.py decide quit-job
python main.py history
python main.py review 1