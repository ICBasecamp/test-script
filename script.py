import time
import sys

def simulate_streaming_data():
    """Simulate streaming data by counting from 1 to 10 with delays."""
    for i in range(1, 11):
        # Print the current number
        print(i, flush=True)
        
        # Sleep for 1 second to simulate delay between data points
        time.sleep(1)

if __name__ == "__main__":
    print("Starting data stream simulation...")
    simulate_streaming_data()
    print("Data stream complete!")
