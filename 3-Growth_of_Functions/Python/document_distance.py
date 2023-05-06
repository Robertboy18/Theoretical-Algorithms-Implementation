import collections as c
import unittest

# Author: Robert Joseph

def document_distance_problem(s1, s2):
    """
    This function computes the cosine similarity between two documents represented
    as strings s1 and s2. It first creates two dictionaries d1 and d2, where the keys
    are words and the values are their respective counts in the documents. It then
    computes the dot product of the two dictionaries and divides by the product of
    their magnitudes to obtain the cosine similarity.
    
    
    The time complexity of this function is O(n^2), where n is the length of the longer document. This is because the function iterates over each word in the two documents and performs a constant number of operations for each pair of words.
    """
    # Split the documents into sequences of words
    l = s1.split()
    t = s2.split()
    
    # Create dictionaries to store the word counts
    d1 = dict(c.OrderedDict(c.Counter(l)))
    d2 = dict(c.OrderedDict(c.Counter(t)))
    
    # Compute the dot product of the two dictionaries
    final_dot = 0
    for (k1,v1) in d1.items():
        for (k2,v2) in d2.items():
            if k1 == k2:
                final_dot += v1*v2
    
    # Divide by the product of the magnitudes to obtain the cosine similarity
    return (final_dot/(len(d1)*len(d2)))*100


class TestDocumentDistanceProblem(unittest.TestCase):
    def test_document_distance_problem(self):
        # Test with identical documents
        s1 = "the quick brown fox"
        s2 = "the quick brown fox"
        self.assertEqual(document_distance_problem(s1, s2), 100.0)

        # Test with different but similar documents
        s1 = "the quick brown fox"
        s2 = "the quick red fox"
        self.assertGreater(document_distance_problem(s1, s2), 70.0)

        # Test with very different documents
        s1 = "the quick brown fox"
        s2 = "john doe is a random name"
        self.assertLess(document_distance_problem(s1, s2), 5.0)


if __name__ == '__main__':
    unittest.main()
