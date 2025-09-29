import unittest
from minifirewall import process_packets # import from my function'


class TestFirewall(unittest.TestCase):
    
    def test_ordering(self):
        packets = [
            (1,5), (2,3), (3,1), (4,3), 
            (5,7), (6,5), (7,1), (8,3), (10,7)]
        
        expected = [(3,1), (7,1), (2,3), (4,3), 
                    (8,3), (1,5), (6,5), (5,7), (10,7)]
        
        self.assertEqual(process_packets(packets), expected)
        
    def test_same_priority(self):
        packets = [(1,3), (2,3), (3,3), (4,3)]
        expected = [(1,3), (2,3), (3,3), (4,3)]
        
        self.assertEqual(process_packets(packets), expected)
        
    def test_empty(self):
        packets = []
        expected = []
        
        self.assertEqual(process_packets(packets), expected)
        
if __name__ == '__main__':
    unittest.main()