# CPU Scheduling Algorithm Simulator

![Python](https://imgshields.io/badge/python-3.x-blue.svg)
![Matplotlib](https://imgshields.io/badge/matplotlib-%231f77b4.svg?style=for-the-badge&logo=matplotlib&logoColor=white)

A comprehensive Python-based simulator for visualizing and comparing various CPU scheduling algorithms. This tool allows users to analyze algorithm performance based on key metrics like average waiting time, average turnaround time, and throughput.

## ✨ Features

* **Multiple Scheduling Algorithms:** Simulates a variety of common CPU schedulers:
    * First-Come, First-Served (FCFS)
    * Shortest Job First (SJF) (Non-Preemptive)
    * Shortest Remaining Time First (SRTF) (Preemptive)
    * Priority Scheduling (Non-Preemptive)
* **Configurable Context Switching Cost:** Allows you to introduce a "switching cost" (time penalty) for context switches to model real-world overhead and analyze its impact on performance.
* **Flexible Input Methods:**
    * **Random Process Generator:** Automatically generate a set of random processes and save them to a CSV file for quick testing and stress tests.
    * **CSV File Input:** Load process data (Arrival Time, Burst Time, Priority) from a `.csv` file for repeatable experiments.
* **In-Depth Performance Analysis:**
    * **Detailed Metrics:** For each algorithm, the simulator calculates and displays Average Waiting Time, Average Turnaround Time, and Throughput.
    * **Text-Based Gantt Chart:** Shows a step-by-step timeline of process execution, including context switches.
* **Automated Graph Generation:**
    * Automatically generates and saves bar charts comparing the performance metrics of all algorithms for a given set of processes.
    * Organizes the output graphs for each simulation run into unique, timestamped folders to keep results tidy.

## 🚀 How to Use

### Prerequisites

* Python 3.x
* Matplotlib library

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/CPU-Scheduling-Simulator.git](https://github.com/YourUsername/CPU-Scheduling-Simulator.git)
    cd CPU-Scheduling-Simulator
    ```

2.  **Install the required library:**
    ```bash
    pip install matplotlib
    ```

### Running the Simulator

Execute the main script from your terminal:
```bash
python main.py
