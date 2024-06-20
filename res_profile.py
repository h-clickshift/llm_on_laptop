import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import psutil
import subprocess
import queue
def get_res_usage(pid):
    p = psutil.Process(pid)
    cpu_usages = []
    mem_usages = []
    while True:
        cpu_usage = p.cpu_percent(interval=1)
        cmd = f"top -l 1 -stats pid,command,mem | awk -v pid={pid} '$1==pid {{print $3; exit}}'"
        mem_usage = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
        if mem_usage.endswith('K'):  # kb
            mem_usage = float(mem_usage[:-1]) / 1024 ** 2
        elif mem_usage.endswith('M'):  # mb
            mem_usage = float(mem_usage[:-1]) / 1024
        elif mem_usage.endswith('G'):  # gb
            mem_usage = float(mem_usage[:-1])
        cpu_usages.append(cpu_usage)
        mem_usages.append(mem_usage)
        yield [cpu_usage, mem_usage]

def update_plot(pid, model):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), gridspec_kw={'hspace': 0.5})
    cpu_usages = []
    mem_usages = []
    cpu = []
    line1, = ax1.plot(cpu, cpu_usages)
    ax1.set_ylim(0, 200)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('CPU Usage (%)')
    ax1.set_title('Dynamic CPU Usage Plot')

    mem = []
    line2, = ax2.plot(mem, cpu_usages)
    ax2.set_ylim(0, 50)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Mem Usage (GB)')
    ax2.set_title('Dynamic Mem Usage Plot')

    plt.show(block=False)

    while True:
        try:
            res_usage = next(get_res_usage(pid))
            cpu_usages.append(res_usage[0])
            mem_usages.append(res_usage[1])
            cpu.append(len(cpu_usages))
            mem.append(len(mem_usages))
            line1.set_data(cpu, cpu_usages)
            ax1.relim()
            ax1.autoscale_view(True, True, True)
            line2.set_data(mem, mem_usages)
            ax2.relim()
            ax2.autoscale_view(True, True, True)
            fig.canvas.draw()
            fig.canvas.flush_events()
            # save img
            plt.savefig(f"{model.split('/')[-1]}.png")
        except queue.Empty:
            pass
