# -*- coding: iso-8859-2 -*-
#
# Fleury's Algorithm implementation
# Dawid Kulig
# dawid.kulig[at]uj.edu.pl

import unittest
from Fleury import *

class TestFleury(unittest.TestCase):

    def setUp(self):
        """
        Przygotowanie testow
        """

        G = {0: [4, 5], 1: [2, 3, 4, 5], 2: [1, 3, 4, 5], 3: [1, 2], 4: [0, 1, 2, 5], 5: [0, 1, 2, 4]}
        self.graph_a = G
        G = {0: [2, 2, 3], 1: [2, 2, 3], 2: [0, 0, 1, 3], 3: [0, 1, 2]}
        self.graph_b = G

    def testEven_degree_nodes(self):
        """
        Testowanie funkcji zwracajacej liste krawedzi parzystych
        """

        fl_a = Fleury(self.graph_a)
        fl_b = Fleury(self.graph_b)

        list_a_expected = [0, 1, 2, 3, 4, 5]
        list_a_result = fl_a.even_degree_nodes(self.graph_a)

        list_b_expected = [2]
        list_b_result = fl_b.even_degree_nodes(self.graph_b)

        self.assertTrue(list_b_expected == list_b_result)
        self.assertTrue(list_a_expected == list_a_result)

    def testIs_eulerian(self):
        """
        Testowanie funkcji sprawdzajacej czy graf jest EULEROWSKI
        """
        fl_a = Fleury(self.graph_a)
        fl_b = Fleury(self.graph_b)

        self.assertTrue(fl_a.is_eulerian(fl_a.even_degree_nodes(self.graph_a), len(self.graph_a)))
        self.assertFalse(fl_b.is_eulerian(fl_b.even_degree_nodes(self.graph_b), len(self.graph_b)))

    def testIs_connected(self):
        """
        Testowanie algorytmu DFS
        """

        fl_a = Fleury(self.graph_a)
        self.assertTrue(fl_a.is_connected(self.graph_b))

    def testConvert_graph(self):
        """
        Testowanie konwersji grafu na liste
        """

        fl_a = Fleury(self.graph_a)
        fl_b = Fleury(self.graph_b)

        converted_a_expected = [(0, 4), (0, 5), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (4, 5), (5, 0), (5, 1), (5, 2), (5, 4)]
        converted_a_result = fl_a.convert_graph(self.graph_a)

        converted_b_expected = [(0, 2), (0, 2), (0, 3), (1, 2), (1, 2), (1, 3), (2, 0), (2, 0), (2, 1), (2, 3), (3, 0), (3, 1), (3, 2)]
        converted_b_result = fl_b.convert_graph(self.graph_b)

        self.assertTrue(converted_a_expected == converted_a_result)
        self.assertTrue(converted_b_expected == converted_b_result)

def runTests():
    """
    Uruchomienie testow
    """

    unittest.main()