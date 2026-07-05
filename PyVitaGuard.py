import psutil

print ("=== System Info ===")

print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
print(f"RAM Usage: {psutil.virtual_memory().percent}%")
print(f"Disk Usage: {psutil.disk_usage('/').percent}%")

print("")
print ("=== Top 10 Processes by Memory ===")

processes = psutil.process_iter()
process_list = []

for process in processes:
    try:
        name = process.name()
        memory = process.memory_info().rss
        process_list.append((name, memory))
    except:
        pass

process_list.sort(key=lambda x: x[1], reverse=True)

for name, memory in process_list[:10]:
    print(f"{name}: {memory / 1024 / 1024:.1f} MB")
