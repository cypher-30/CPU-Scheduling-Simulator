import csv
import random
import os
import matplotlib.pyplot as plt
from typing import List, Dict
from datetime import datetime


# NEW: Function to generate random processes and save them to a CSV file
def generate_random_processes_to_csv(num_processes: int, filename: str):
    """Generates a list of random processes and writes them to a CSV file."""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ArrivalTime', 'BurstTime', 'Priority'])

        current_arrival_time = 0
        for _ in range(num_processes):
            current_arrival_time += random.randint(0, 3)
            burst_time = random.randint(1, 20)
            priority = random.randint(1, 10)
            writer.writerow([current_arrival_time, burst_time, priority])
    print(f"✅ Successfully generated {num_processes} random processes in '{filename}'")


def get_input_from_file(filename: str) -> List[Dict]:
    """Reads process data from the specified CSV file."""
    processes = []
    try:
        with open(filename, mode='r') as infile:
            reader = csv.reader(infile)
            next(reader)  # Skip header
            pid_counter = 1
            for row in reader:
                try:
                    arrival, burst, priority = map(int, row)
                    if arrival < 0 or burst <= 0 or priority < 0:
                        print(f"Warning: Invalid data in row for PID {pid_counter}. Skipping.")
                        continue
                    processes.append({
                        "PID": pid_counter, "ArrivalTime": arrival, "BurstTime": burst, "Priority": priority
                    })
                    pid_counter += 1
                except (ValueError, IndexError):
                    print(f"Warning: Malformed row for PID {pid_counter}. Skipping.")
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
    return processes


# --- Metrics, Algorithms, and Formatting (remain the same) ---
def calculate_metrics(processes: List[Dict]) -> Dict:
    n = len(processes)
    if n == 0: return {"average_waiting_time": 0, "average_turnaround_time": 0, "throughput": 0}
    total_waiting_time = sum(p['WaitingTime'] for p in processes)
    total_turnaround_time = sum(p['TurnaroundTime'] for p in processes)
    last_completion_time = max(p['CompletionTime'] for p in processes)
    makespan = last_completion_time - min(p['ArrivalTime'] for p in processes)
    return {"average_waiting_time": total_waiting_time / n, "average_turnaround_time": total_turnaround_time / n,
            "throughput": n / makespan if makespan > 0 else float('inf')}


def fcfs(processes: List[Dict], switching_cost: int):
    procs = [p.copy() for p in processes]
    procs.sort(key=lambda x: (x['ArrivalTime'], x['PID']))
    time, gantt, last_pid = 0, [], None
    for p in procs:
        if time < p['ArrivalTime']:
            time = p['ArrivalTime']
            last_pid = None
        if last_pid is not None and switching_cost > 0:
            gantt.append(('Switch', time, time + switching_cost))
            time += switching_cost
        p['StartTime'], p['CompletionTime'] = time, time + p['BurstTime']
        p['TurnaroundTime'], p['WaitingTime'] = p['CompletionTime'] - p['ArrivalTime'], p['CompletionTime'] - p[
            'ArrivalTime'] - p['BurstTime']
        gantt.append((p['PID'], p['StartTime'], p['CompletionTime']))
        time, last_pid = p['CompletionTime'], p['PID']
    return procs, calculate_metrics(procs), gantt


def sjf(processes: List[Dict], switching_cost: int):
    procs = [p.copy() for p in processes]
    time, done_count, gantt, last_pid = 0, 0, [], None
    while done_count < len(procs):
        available = [p for p in procs if p.get('StartTime') is None and p['ArrivalTime'] <= time]
        if not available:
            time = min(p['ArrivalTime'] for p in procs if p.get('StartTime') is None)
            last_pid = None
            continue
        p = min(available, key=lambda x: x['BurstTime'])
        if last_pid is not None and switching_cost > 0:
            gantt.append(('Switch', time, time + switching_cost))
            time += switching_cost
        p['StartTime'], p['CompletionTime'] = time, time + p['BurstTime']
        p['TurnaroundTime'], p['WaitingTime'] = p['CompletionTime'] - p['ArrivalTime'], p['CompletionTime'] - p[
            'ArrivalTime'] - p['BurstTime']
        gantt.append((p['PID'], p['StartTime'], p['CompletionTime']))
        time, last_pid, done_count = p['CompletionTime'], p['PID'], done_count + 1
    return procs, calculate_metrics(procs), gantt


def srtf(processes: List[Dict], switching_cost: int):
    procs = [p.copy() for p in processes]
    for p in procs: p['RemainingTime'] = p['BurstTime']
    time, done_count, gantt, last_pid = 0, 0, [], None
    while done_count < len(procs):
        available = [p for p in procs if p['ArrivalTime'] <= time and p['RemainingTime'] > 0]
        if not available:
            time = min(p['ArrivalTime'] for p in procs if p['RemainingTime'] > 0)
            last_pid = None
            continue
        p = min(available, key=lambda x: x['RemainingTime'])
        if p['PID'] != last_pid and last_pid is not None and switching_cost > 0:
            gantt.append(['Switch', time, time + switching_cost])
            time += switching_cost
            available = [pr for pr in procs if pr['ArrivalTime'] <= time and pr['RemainingTime'] > 0]
            if not available: continue
            p = min(available, key=lambda x: x['RemainingTime'])
        if p.get('StartTime') is None: p['StartTime'] = time
        if not gantt or gantt[-1][0] != p['PID'] or gantt[-1][2] != time:
            gantt.append([p['PID'], time, time + 1])
        else:
            gantt[-1][2] = time + 1
        p['RemainingTime'] -= 1
        last_pid, time = p['PID'], time + 1
        if p['RemainingTime'] == 0:
            p['CompletionTime'] = time
            p['TurnaroundTime'], p['WaitingTime'] = p['CompletionTime'] - p['ArrivalTime'], p['CompletionTime'] - p[
                'ArrivalTime'] - p['BurstTime']
            done_count += 1
            last_pid = None
    return procs, calculate_metrics(procs), gantt


def priority_scheduling(processes: List[Dict], switching_cost: int):
    procs = [p.copy() for p in processes]
    time, done_count, gantt, last_pid = 0, 0, [], None
    while done_count < len(procs):
        available = [p for p in procs if p.get('StartTime') is None and p['ArrivalTime'] <= time]
        if not available:
            time = min(p['ArrivalTime'] for p in procs if p.get('StartTime') is None)
            last_pid = None
            continue
        p = min(available, key=lambda x: (x['Priority'], x['ArrivalTime']))
        if last_pid is not None and switching_cost > 0:
            gantt.append(('Switch', time, time + switching_cost))
            time += switching_cost
        p['StartTime'], p['CompletionTime'] = time, time + p['BurstTime']
        p['TurnaroundTime'], p['WaitingTime'] = p['CompletionTime'] - p['ArrivalTime'], p['CompletionTime'] - p[
            'ArrivalTime'] - p['BurstTime']
        gantt.append((p['PID'], p['StartTime'], p['CompletionTime']))
        time, last_pid, done_count = p['CompletionTime'], p['PID'], done_count + 1
    return procs, calculate_metrics(procs), gantt


def format_results(name: str, results: List[Dict], metrics: Dict, gantt: List):
    print("\n" + "=" * 85)
    print(f"✅ RESULTS FOR: {name} Scheduling Algorithm")
    print("=" * 85)
    print(
        f"{'PID':<5} {'Arrival':<10} {'Burst':<10} {'Priority':<10} {'Start':<10} {'Completion':<12} {'Turnaround':<12} {'Waiting':<10}")
    print("-" * 85)
    results.sort(key=lambda p: p['PID'])
    for p in results: print(
        f"{p['PID']:<5} {p['ArrivalTime']:<10} {p['BurstTime']:<10} {p.get('Priority', '-'):<10} {p.get('StartTime', 'N/A'):<10} {p.get('CompletionTime', 'N/A'):<12} {p.get('TurnaroundTime', 'N/A'):<12} {p.get('WaitingTime', 'N/A'):<10}")
    print("-" * 85)
    print("\n📊 Summary Metrics:")
    print(f"  Average Waiting Time      : {metrics['average_waiting_time']:.2f}")
    print(f"  Average Turnaround Time   : {metrics['average_turnaround_time']:.2f}")
    print(f"  Throughput                : {metrics['throughput']:.2f} processes/unit time")
    print("\n📈 Gantt Chart:")
    print(" | ".join([f"Switch({s}→{e})" if pid == 'Switch' else f"P{pid}({s}→{e})" for pid, s, e in gantt]))
    print("=" * 85)


def generate_comparison_graphs(all_metrics: List[Dict], output_folder: str):
    if not all_metrics: return
    os.makedirs(output_folder, exist_ok=True)
    sorted_metrics = sorted(all_metrics, key=lambda x: x['name'])
    algo_names = [result['name'] for result in sorted_metrics]

    # Plot 1: Waiting Time
    plt.figure(figsize=(10, 6))
    bars = plt.bar(algo_names, [r['metrics']['average_waiting_time'] for r in sorted_metrics], color='skyblue')
    plt.ylabel('Time Units');
    plt.title('Average Waiting Time Comparison')
    for bar in bars: plt.text(bar.get_x() + bar.get_width() / 2.0, bar.get_height(), f'{bar.get_height():.2f}',
                              va='bottom', ha='center')
    plt.tight_layout();
    plt.savefig(os.path.join(output_folder, 'average_waiting_time_comparison.png'));
    plt.close()

    # Plot 2: Turnaround Time
    plt.figure(figsize=(10, 6))
    bars = plt.bar(algo_names, [r['metrics']['average_turnaround_time'] for r in sorted_metrics], color='lightcoral')
    plt.ylabel('Time Units');
    plt.title('Average Turnaround Time Comparison')
    for bar in bars: plt.text(bar.get_x() + bar.get_width() / 2.0, bar.get_height(), f'{bar.get_height():.2f}',
                              va='bottom', ha='center')
    plt.tight_layout();
    plt.savefig(os.path.join(output_folder, 'average_turnaround_time_comparison.png'));
    plt.close()

    # Plot 3: Throughput
    plt.figure(figsize=(10, 6))
    bars = plt.bar(algo_names, [r['metrics']['throughput'] for r in sorted_metrics], color='mediumseagreen')
    plt.ylabel('Processes / Time Unit');
    plt.title('Throughput Comparison')
    for bar in bars: plt.text(bar.get_x() + bar.get_width() / 2.0, bar.get_height(), f'{bar.get_height():.2f}',
                              va='bottom', ha='center')
    plt.tight_layout();
    plt.savefig(os.path.join(output_folder, 'throughput_comparison.png'));
    plt.close()

    print(f"\n\n🎉 Success! Comparison graphs have been saved to the '{output_folder}' directory.")


def main():
    print("Welcome to the Advanced CPU Scheduling Algorithm Simulator! 👨‍💻")
    processes = []

    while True:
        choice = input(
            "\nChoose an option:\n  [1] Generate new random processes into a CSV\n  [2] Load processes from an existing CSV file\nYour choice: ")
        if choice == '1':
            try:
                num_procs = int(input("How many processes to generate? "))
                if num_procs <= 0: raise ValueError
                filename = "processes.csv"
                generate_random_processes_to_csv(num_procs, filename)
                processes = get_input_from_file(filename)
                if processes: break
            except ValueError:
                print("❌ Invalid number. Please enter a positive integer.")
        elif choice == '2':
            filename = input("Enter the CSV filename to load (e.g., processes.csv): ")
            processes = get_input_from_file(filename)
            if processes: break
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")

    try:
        switching_cost = int(input("\nEnter the context switching cost (e.g., 1): "))
        if switching_cost < 0: switching_cost = 0
    except ValueError:
        switching_cost = 0

    # MODIFIED: Create a nested folder structure
    parent_folder = "comparison_graphs"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_folder_name = f"run_{timestamp}"
    output_folder = os.path.join(parent_folder, run_folder_name)

    print(f"\n📈 Results and graphs for this run will be saved in: '{output_folder}'")

    algorithm_map = {"FCFS": fcfs, "SJF": sjf, "SRTF": srtf, "Priority": priority_scheduling}
    all_metrics_for_graphing = []

    for name, func in algorithm_map.items():
        results, metrics, gantt = func([p.copy() for p in processes], switching_cost)
        format_results(name, results, metrics, gantt)
        all_metrics_for_graphing.append({'name': name, 'metrics': metrics})

    generate_comparison_graphs(all_metrics_for_graphing, output_folder)


if __name__ == "__main__":
    main()