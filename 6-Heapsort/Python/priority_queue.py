import unittest
from queue import PriorityQueue

# Author: Robert Joseph

def min_max_priority_tests():
    # Create a priority queue
    pq = PriorityQueue()

    # Insert elements with their priorities
    pq.put((1, 3))
    pq.put((4, 4))
    pq.put((10, 4))

    # Increase the priority of an element
    # Find the element with the desired priority and update its value
    while not pq.empty():
        element = pq.get()
        if element[0] == 1:
            updated_element = (2, element[1])
            break
    pq.put(updated_element)

    # Get the maximum element
    maximum_element = pq.get()
    print(maximum_element)

    # Insert another element
    pq.put((100, 4))

    # Convert the priority queue to a min-max priority queue
    length = pq.qsize()
    while length:
        element = pq.get()
        converted_element = (-element[0], element[1])
        pq.put(converted_element)
        length -= 1

    # Print the min-max priority queue
    print(pq.queue)

    # Extract the maximum element
    extracted_element = pq.get()
    print(extracted_element)


class TestMinMaxPriority(unittest.TestCase):
    def test_min_max_priority(self):
        pq = PriorityQueue()
        pq.put((1, 3))
        pq.put((4, 4))
        pq.put((10, 4))
        
        self.assertEqual(pq.get(), (1, 3))  # Check maximum element
        
        pq.put((100, 4))
        
        pq_converted = PriorityQueue()
        while not pq.empty():
            element = pq.get()
            converted_element = (-element[0], element[1])
            pq_converted.put(converted_element)
        
        self.assertEqual(pq_converted.queue, [(-10, 4), (-4, 4), (-1, 3)])  # Check converted min-max priority queue
        
        self.assertEqual(pq_converted.get(), (-10, 4))  # Check extracted maximum element


if __name__ == '__main__':
    unittest.main()
