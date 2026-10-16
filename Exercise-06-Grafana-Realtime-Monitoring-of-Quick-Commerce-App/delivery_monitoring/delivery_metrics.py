from prometheus_client import start_http_server, Summary, Gauge
import random
import time

# Metrics Definition
total_deliveries = Gauge("total_deliveries", "Total number of deliveries - MANOJ MURTHY S (1BM24IS411)")
pending_deliveries = Gauge("pending_deliveries", "Number of pending deliveries")
on_the_way_deliveries = Gauge("on_the_way_deliveries", "Number of deliveries on the way")
average_delivery_time = Summary("average_delivery_time", "Average delivery time in seconds")

def simulate_delivery():
    pending = random.randint(10, 25)  # Triggers HighPendingDeliveries alert threshold (>10)
    on_the_way = random.randint(5, 20)
    delivered = random.randint(30, 70)
    avg_time = random.uniform(20, 50)

    total = pending + on_the_way + delivered

    print(f"[MANOJ MURTHY S - 1BM24IS411] [DEBUG] Total deliveries: {total}")
    print(f"[DEBUG] Pending deliveries: {pending}")
    print(f"[DEBUG] On-the-way deliveries: {on_the_way}")
    print(f"[DEBUG] Average delivery time: {avg_time:.2f} seconds")

    total_deliveries.set(total)
    pending_deliveries.set(pending)
    on_the_way_deliveries.set(on_the_way)
    average_delivery_time.observe(avg_time)

if __name__ == "__main__":
    print("[INFO] Starting Prometheus metrics HTTP server on port 8000...")
    start_http_server(8000, addr="0.0.0.0")
    print("[INFO] HTTP server started at http://localhost:8000/metrics. Simulating quick-commerce deliveries...")
    while True:
        simulate_delivery()
        print("[INFO] Sleeping for 2 seconds...")
        time.sleep(2)
