OS Memory Simulator 🖥️

An interactive memory management simulator demonstrating segmentation, paging, demand paging, and page replacement algorithms (LRU & Optimal).
Built with Python (backend) and React + Tailwind (frontend) for a cross-platform experience.

Features
Feature	Description
Algorithms	LRU & Optimal
Memory Management	Segmentation, Paging, Demand Paging
Visualization	Step-by-step memory states
Metrics	Page Hits & Page Faults
Interface	React + Tailwind frontend
Backend	Python Flask API
Demo

Input:

Page Reference: 7 0 1 2 0 3 0 4
Frames: 3
Algorithm: LRU


Output:

Step 1: [7]
Step 2: [7, 0]
Step 3: [7, 0, 1]
Step 4: [2, 0, 1]
...
Page Faults: 6
Page Hits: 2

Tech Stack

Python 3 – Simulation logic

Flask – REST API backend

React – Interactive web UI

Tailwind CSS – Styling & responsive design

Run Locally
Backend
cd backend
pip install flask
python memory_simulator.py

Frontend
cd frontend
npm install
npm start


Access at http://localhost:3000
