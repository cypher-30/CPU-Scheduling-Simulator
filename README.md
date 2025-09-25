CPU Scheduling Algorithm Simulator
A comprehensive Python-based simulator for visualizing and comparing various CPU scheduling algorithms. This tool allows users to analyze algorithm performance based on key metrics like average waiting time, average turnaround time, and throughput.

✨ Features
Multiple Scheduling Algorithms: Simulates a variety of common CPU schedulers:

First-Come, First-Served (FCFS)

Shortest Job First (SJF) (Non-Preemptive)

Shortest Remaining Time First (SRTF) (Preemptive)

Priority Scheduling (Non-Preemptive)

Configurable Context Switching Cost: Allows you to introduce a "switching cost" (time penalty) for context switches to model real-world overhead and analyze its impact on performance.

Flexible Input Methods:

Random Process Generator: Automatically generate a set of random processes and save them to a CSV file for quick testing and stress tests.

CSV File Input: Load process data (Arrival Time, Burst Time, Priority) from a .csv file for repeatable experiments.

In-Depth Performance Analysis:

Detailed Metrics: For each algorithm, the simulator calculates and displays Average Waiting Time, Average Turnaround Time, and Throughput.

Text-Based Gantt Chart: Shows a step-by-step timeline of process execution, including context switches.

Automated Graph Generation:

Automatically generates and saves bar charts comparing the performance metrics of all algorithms for a given set of processes.

Organizes the output graphs for each simulation run into unique, timestamped folders to keep results tidy.

🚀 How to Use
Prerequisites
Python 3.x

Matplotlib library

Installation
Clone the repository:

git clone [https://github.com/YourUsername/CPU-Scheduling-Simulator.git](https://github.com/YourUsername/CPU-Scheduling-Simulator.git)
cd CPU-Scheduling-Simulator

Install the required library:
This project requires matplotlib for generating graphs. You can install it using pip:

pip install matplotlib

Running the Simulator
Execute the main script from your terminal:

python main.py

(Assuming your main script is named main.py)

The program will then present you with a menu:

Generate new random processes: This will prompt you for the number of processes to create and will save them in processes.csv. It then immediately runs the simulation using this new data.

Load processes from an existing CSV file: This will ask for the filename of your CSV. The CSV file must have three columns in this order: ArrivalTime, BurstTime, Priority.

After loading the data, you will be prompted to enter a context switching cost (e.g., 1 for a small cost or 0 for none).

The simulator will then run all algorithms, print the results to the console, and save the comparison graphs.

📁 Project Structure
CPU-Scheduling-Simulator/
│
├── main.py                     # The main Python script for the simulator.
│
├── processes.csv               # Default CSV file for process data. Can be generated or user-created.
│
├── comparison_graphs/          # Parent directory for all generated output.
│   └── run_YYYY-MM-DD_HH-MM-SS/  # Each simulation run creates a unique folder.
│       ├── average_waiting_time_comparison.png
│       ├── average_turnaround_time_comparison.png
│       └── throughput_comparison.png
│
└── README.md                   # This file.

🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or want to add new features (like Round Robin or Preemptive Priority scheduling), please feel free to fork the repository and submit a pull request.

Fork the Project

Create your Feature Branch (git checkout -b feature/NewAlgorithm)

Commit your Changes (git commit -m 'Add some NewAlgorithm')

Push to the Branch (git push origin feature/NewAlgorithm)

Open a Pull Request
