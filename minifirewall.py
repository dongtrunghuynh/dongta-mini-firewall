import sys

   
def process_packets(packet):
    """Sorting the packets by priority. The packets come as a tuple (id, priority)
    1 is the highest and 10 is the lowest for both priority and id
    ID must be unique
    """
    return sorted(packet, key=lambda x: (x[1], x[0])) # x[1] is the position of the priority, x[0] is the position of the id

def batch_process(packets, batch_size=10):
    """Process packets in batches of a specified size."""
    for i in range(0, len(packets), batch_size):
        yield process_packets(packets[i:i + batch_size])

def read_from_file(file_path):
    """Read packets from a file. Each line in the file should contain 'serial,priority'."""
    packets = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith("serial"):
                continue
            try:
                serial, priority = map(int, line.split(","))
                packets.append((serial, priority))
            except ValueError:
                print(f"Invalid line format: {line.strip()}. Skipping.")
    return packets
                

def main():
    # check a file is provided
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        packets = read_from_file(file_path)
    else:
        print("Enter packets as 'serial,priority'. Type 'done' when finished.")
        while True:
            user_input = input ("> ")
            if user_input.lower() == "done":
                break
            try:
                serial, priority = map(int, user_input.split(","))
                packet = (serial,priority)
                if packet in packets:
                    print(f"Packet with id {serial} already exists. Please enter a unique id.")
                else:
                    packets.add(packet)
            except ValueError:
                print("Invalid input. Please enter in the format 'id,priority' or 'done' to finish.")

    print("\nOrdered Packets (by batch of 10):")
    for batch_num, batch in enumerate(batch_process(packets), start=1):
        print(f"Batch {batch_num}: {batch}")
        for serial, priority in batch:
            print(f"Processing packet with id {serial} and priority {priority}")

if __name__ == "__main__":
    main() 

