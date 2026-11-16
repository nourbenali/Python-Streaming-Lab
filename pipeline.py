"""
pipeline.py
----------------
This file launches BOTH producer and consumer using Python threads to simulate
a real streaming pipeline.

"""

import threading
from queue import Queue
from producer import CSVProducer
from consumer import Consumer

def main():
    """
    TODO:
    - Create the shared queue.
    - Instantiate the producer and consumer.
    - Create a thread for each.
    - Start both threads.
    - Optionally join them so the program runs continuously.

    The students should run:
        python pipeline.py
    and observe live streaming behavior.
    """
    # Create the shared queue
    shared_queue = Queue()

    # Instantiate the producer and consumer
    producer = CSVProducer("/Users/veronicacornwell/Streaming_Code/Python-Streaming-Lab/transactions.csv", shared_queue, delay=1.0)
    consumer = Consumer(shared_queue)

    # Create threads for producer and consumer
    producer_thread = threading.Thread(target=producer.start)
    consumer_thread = threading.Thread(target=consumer.start)

    # Start both threads
    producer_thread.start()
    consumer_thread.start()


if __name__ == "__main__":
    print("Starting the Python Streaming Pipeline...")
    main()
