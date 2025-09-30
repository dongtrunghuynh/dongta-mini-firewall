import sys
import re

BATCH_SIZE = 10

def process_packets(packets):
    """Sort packets by priority and serial number if priorities are the same.
    1 is the highest priority.

    """
    return sorted(packets, key=lambda x: (x[1], x[0]))

def batch_process(packets, batch_size=BATCH_SIZE):
    """Yield packdst in batches of batch_size, then sorted within each batch.

    """
    for i in range(0, len(packets), batch_size):
        batch = packets[i:i + batch_size]
        yield process_packets(batch)

def read_from_file(file_path):
    " Read file from a path, ignoring all whitespaces and commas"
    
    packets = []
    with open(file_path, "r", encoding="utf-8-sig") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#") or re.match(r'(?i)serial,priority', line):
                continue
            # split on commas or whitespace
            parts = re.split(r'[,\s]+', line)
            if len(parts) != 2 or not all(p.isdigit() for p in parts):
                continue # skip malformed lines silently
            serial, priority = map(int, parts)
            if not (1 <= priority <= 10):
                print(f"Skipping invalid priority {priority} for packet id {serial} on line {line}. Must be 1-10.")
                continue # skip invalid priorities silently
            packet = (serial, priority)
    return packets

def main():
    packets = []
    if len(sys.argv) > 1:
        file_path = sys.argv[1:]
        packets = read_from_file(file_path)
    else:
        print(f"Enter up to {BATCH_SIZE} packets 'serial,priority' (type 'done' to finish): ")
        while True:
            if len(packets) >= BATCH_SIZE:
                print(f"Packet limit reached {BATCH_SIZE}. No more packets can be added")
                break
            user_input = input("> ").strip()
            if user_input.lower() == 'done':
                break
            if not user_input:
                continue
            parts = re.split(r'[,\s]+', user_input)
            if len(parts) != 2 or not all(p.isdigit() for p in parts):
                print("Invalid input. Enter as 'serial,priority'")
                continue
            serial, priority = map(int, parts)
            if not (1 <= priority <= 10):
                print(f"Duplicate packet {packet}. Ignored.")
            else:
                packets.append(packet)
    if not packets:
        print("No valid packets to process.")
        return
        
    
    # process and print results in batches
    print("\nOrdred Packets (by batch):")
    for batch_num, batch in enumerate(batch_process(packets), start=1):
        print(f"\nBatch {batch_num}")
        for serial, priority in batch:
            print(f"{serial},{priority}")
            
if __name__ == "__main__":
    main()
