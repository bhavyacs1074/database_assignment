import matplotlib.pyplot as plt
import csv

read_ratios = []
logical_reads = []
logical_writes = []
physical_reads = []
physical_writes = []

with open("results.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if not row:
            continue
        rratio, lread, lwrite, pread, pwrite = map(int, row)
        read_ratios.append(rratio)
        logical_reads.append(lread)
        logical_writes.append(lwrite)
        physical_reads.append(pread)
        physical_writes.append(pwrite)

plt.figure(figsize=(8, 6))
plt.plot(read_ratios, logical_reads, marker='o', label='Logical Reads')
plt.plot(read_ratios, logical_writes, marker='o', label='Logical Writes')
plt.plot(read_ratios, physical_reads, marker='o', label='Physical Reads')
plt.plot(read_ratios, physical_writes, marker='o', label='Physical Writes')

plt.title("I/O Statistics vs Read/Write Ratio")
plt.xlabel("Read Ratio (%)")
plt.ylabel("I/O Count")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
