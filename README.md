# CPU Scheduling Algorithm Simulator

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Matplotlib](https://img.shields.io/badge/matplotlib-%231f77b4.svg?style=for-the-badge&logo=matplotlib&logoColor=white)

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
    git clone [https://github.com/cypher-30/CPU-Scheduling-Simulator.git](https://github.com/cypher-30/CPU-Scheduling-Simulator.git)
    cd CPU-Scheduling-Simulator
    ```

2.  **Install the required library:**
    This project requires `matplotlib` for generating graphs. You can install it using pip:
    ```bash
    pip install matplotlib
    ```

### Running the Simulator

Execute the main script from your terminal:
```bash
python main.py
````

*(Assuming your main script is named `main.py`)*

The program will then present you with a menu to either generate random processes or load them from a CSV. After the data is loaded, you will be prompted for a **context switching cost**.

## 📁 Project Structure

```
CPU-Scheduling-Simulator/
│
├── main.py
├── processes.csv
│
├── comparison_graphs/          # Ignored by Git, won't be uploaded.
│   └── run_YYYY-MM-DD_HH-MM-SS/
│       ├── average_waiting_time_comparison.png
│       ├── ...
│
├── .gitignore                  # Tells Git to ignore the graphs folder.
└── README.md
```

## 🤝 Contributing

Contributions are welcome\! If you have suggestions for improvements or want to add new features (like Round Robin or Preemptive Priority scheduling), please feel free to fork the repository and submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/NewAlgorithm`)
3.  Commit your Changes (`git commit -m 'Add some NewAlgorithm'`)
4.  Push to the Branch (`git push origin feature/NewAlgorithm`)
5.  Open a Pull Request

<!-- end list -->

```
```
