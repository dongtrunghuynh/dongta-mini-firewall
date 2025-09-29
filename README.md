# minifirewall.py
### A simple python program that simulates a mini firewall which filters and processes network packets.

### The firewally enforces these rules:
- Each packet has a Serial Number and a Priority
- Priority 1 is highest, Priority 10 is lowest.
- Packets are sorted by prioirty first, then serial number if priorities are equal
- Duplicate packets (same (serial, priority) pair) are ignored.
- At most 10 packets can be processed at a time.

## How to run
git clone https://github.com/your-username/mini-firewall.git
cd minifirewall

## run the firewall
python minifirewall.py

## enter the packets in the format of serial,priority. program will stop once you enter 'done'

### examples
Enter up to 10 packets as 'serial,priority' (type 'done' to finish):
- > 1,5
- > 2,3
- > 3,1
- > 4,3
- > 5,7
- > 6,10
- > 10,1
- > 10,2
- > done


### output
Ordered Packets:
- Serial: 3, Priority: 1
- Serial: 10, Priority: 1
- Serial: 10, Priority: 2
- Serial: 2, Priority: 3
- Serial: 4, Priority: 3
- Serial: 1, Priority: 5
- Serial: 5, Priority: 7
- Serial: 6, Priority: 10

### run the firewall with a csv file

py or python minifirewall.py packets.csv 
