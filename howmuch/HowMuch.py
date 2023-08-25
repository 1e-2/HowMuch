import psutil
import os
import argparse
from tqdm import tqdm
import matplotlib.pyplot as plt

def get_size(bytes, suffix="B"):
    """Convert bytes to human-readable formats (e.g., KB, MB, GB, etc.)."""
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f} {unit}{suffix}"
        bytes /= factor

def get_file_size_for_extensions(drive, extensions):
    """Get the total size of files with specific extensions in a drive."""
    total_size = 0
    for dirpath, dirnames, filenames in tqdm(os.walk(drive), desc=f"Scanning {drive}", unit="dir"):
        for file in filenames:
            if any(file.endswith(ext) for ext in extensions):
                total_size += os.path.getsize(os.path.join(dirpath, file))
    return total_size

parser = argparse.ArgumentParser(description="Analyze disk space used by specific file extensions.")
parser.add_argument("--scan", metavar="PATH", type=str, help="Specify a folder or drive to scan. If not provided, all drives will be scanned.")
args = parser.parse_args()

if args.scan:
    partitions = [type('', (), {"mountpoint": args.scan})()]
else:
    partitions = psutil.disk_partitions()

total_space = 0
total_free_space = 0
total_ckptsafetensors_size = 0

log_output = []

for partition in partitions:
    usage = psutil.disk_usage(partition.mountpoint)
    ckptsafetensors_size = get_file_size_for_extensions(partition.mountpoint, [".ckpt", ".safetensors"])
    drive_name = partition.device if hasattr(partition, 'device') else args.scan
    log_output.append(f"\nDrive {drive_name}:")
    log_output.append(f"  Total Space: {get_size(usage.total)}")
    log_output.append(f"  Space taken by .ckpt and .safetensors files: {get_size(ckptsafetensors_size)}")
    log_output.append(f"  Free Space: {get_size(usage.free)}")
    total_space += usage.total
    total_free_space += usage.free
    total_ckptsafetensors_size += ckptsafetensors_size

log_output.append("\nTOTAL space taken by all drives: {}".format(get_size(total_space)))
log_output.append("TOTAL free space across all drives: {}".format(get_size(total_free_space)))
log_output.append("TOTAL space taken by .ckpt and .safetensors files: {}".format(get_size(total_ckptsafetensors_size)))
log_output.append("\nNote: The sizes may not match exactly with Windows File Explorer due to system reserved space.")

# Print and save to txt
with open('HowMuch_output.txt', 'w') as f:
    for line in log_output:
        print(line)
        f.write(line + '\n')

# Generate Chart
drives = [partition.device if hasattr(partition, 'device') else args.scan for partition in partitions]
total_spaces = [psutil.disk_usage(partition.mountpoint).total for partition in partitions]
ckpt_safetensor_sizes = [get_file_size_for_extensions(partition.mountpoint, [".ckpt", ".safetensors"]) for partition in partitions]
free_spaces = [psutil.disk_usage(partition.mountpoint).free for partition in partitions]

bar_width = 0.25
r1 = range(len(drives))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

# Adjusted colors here:
plt.bar(r1, total_spaces, color='pink', width=bar_width, edgecolor='grey', label='Total Space')
plt.bar(r2, ckpt_safetensor_sizes, color='purple', width=bar_width, edgecolor='grey', label='.ckpt & .safetensors Size')
plt.bar(r3, free_spaces, color='g', width=bar_width, edgecolor='grey', label='Free Space')

plt.xlabel('Drives', fontweight='bold')
plt.xticks([r + bar_width for r in range(len(drives))], drives)
plt.legend()
plt.savefig('HowMuch_chart.png')
plt.show()
