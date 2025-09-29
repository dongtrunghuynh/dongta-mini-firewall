def process_packets(packet):
    """Sorting the packets by priority. The packets come as a tuple (id, priority)
    1 is the highest and 10 is the lowest for both priority and id
    ID must be unique
    """
    return sorted(packet, key=lambda x: (x[1], x[0])) # x[1] is the position of the priority, x[0] is the position of the id

def main():
    print("Enter packets as 'serial,priority'. Type 'done' when finished.")
    packets = set()
    while True:
        if len(packets)  >= 10:
            print("Maximum of 10 packets reached.")
            break
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
    
    packet_list = list(packets)
    
    result = process_packets(packet_list)
    print("\nOrdered Packets: ")
    for serial, priority in result:
        print(f"Serial: {serial}, Priority: {priority}")

if __name__ == "__main__":
    main() 

