#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
#
# Fleury's Algorithm implementation
# Dawid Kulig
# dawid.kulig[at]uj.edu.pl

import copy

class FleuryException(Exception):
    def __init__(self, message):
        super(FleuryException, self).__init__(message)
        self.message = message

class Fleury:

    COLOR_WHITE = 'white'
    COLOR_GRAY  = 'gray'
    COLOR_BLACK = 'black'

    def __init__(self, graph):
        """
        Funckaj przypisująca graf
        :param graph:
        :return:
        """

        self.graph = graph

    def run(self):
        """
        Funkcja uruchamiajaca działanie algorytmu
        :return:
        """

        print '** Running Fleury algorithm for graph : ** \n'
        for v in self.graph:
            print v, ' => ', self.graph[v]
        print '\n'
        output = None
        try:
            output = self.fleury(self.graph)
        except FleuryException as (message):
            print message

        if output:
            print '** Found Eulerian Cycle : **\n'
            for v in output:
                print v
        print '\n** DONE **'

    def is_connected(self, G):
        """
        Funkcja sprawdzajaca czy podany graf jest spojny
        za pomoca algorytmu DFS ze stosem
        :param G: GRAF
        :return: True / False
        """

        start_node = list(G)[0]
        color = {}
        iterator = 0;
        for v in G:
            color[v] = Fleury.COLOR_WHITE
        color[start_node] = Fleury.COLOR_GRAY
        S = [start_node]
        while len(S) != 0:
            u = S.pop()
            for v in G[u]:
                if color[v] == Fleury.COLOR_WHITE:
                    color[v] = Fleury.COLOR_GRAY
                    S.append(v)
                color[u] = Fleury.COLOR_BLACK
        return list(color.values()).count(Fleury.COLOR_BLACK) == len(G)

    def even_degree_nodes(self, G):
        """
        Funkcja, ktora zwraca liczbe parzystych wierzcholkow w grafie
        Returns: lista parzystych wierzcholkow w grafie
        """

        even_degree_nodes = []
        for u in G:
            if len(G[u]) % 2 == 0:
                even_degree_nodes.append(u)
        return even_degree_nodes


    def is_eulerian(self, even_degree_odes, graph_len):
        """
        Sprawdzenie czy podany graf nieskierowany jest grafem Eulerowskim
        Returns: true / false
        """

        return graph_len - len(even_degree_odes) == 0


    def convert_graph(self, G):
        """
        Funkcja, ktora zmienia strukture grafu.
        Przkladowe dane wejsciowe {0: [4, 5], 1: [2, 3, 4, 5]}
        Returns: [(0, 4), (0, 5), (1, 2), (1, 3), (1, 4), (1, 5)]
        """

        links = []
        for u in G:
            for v in G[u]:
                links.append((u, v))
        return links


    def fleury(self, G):
        """
        Funkcja znajdujaca cykl eulerowski w podanym grafie
        Returns: lista krawedzi (cykl eulerowski)
        """

        edn = self.even_degree_nodes(G)
        # sprawdzenie, czy graf jest grafem eulerowskim
        if not self.is_eulerian(edn, len(G)):
            raise FleuryException('Podany graf nie jest grafem Eulerowskim!')
        g = copy.copy(G)
        cycle = []
        # wybieramy dowolny wierzchołek w grafie o niezerowym stopniu
        u = edn[0]
        while len(self.convert_graph(g)) > 0:
            current_vertex = u
            #for u in g[current_vertex]: # NIEDOBRE, BO ZMIENIA SIE W PETLI
            for u in list(g[current_vertex]): # OSOBNA KOPIA
                g[current_vertex].remove(u)
                g[u].remove(current_vertex)
                # wybieramy krawędź, która nie jest mostem
                # (przejście przez most oznacza brak możliwości powrotu
                # do tego wierzchołka
                # zatem jeśli zostały w nim nieodwiedzone krawędzie,
                # to tych krawędzi już byśmy nie odwiedzili
                # i cykl Eulera nie zostałby znaleziony)
                bridge = not self.is_connected(g)
                if bridge:
                    # nie ma innego wyboru (krawedz - most)
                    # zapamiętujemy tę krawędź na liście lub na stosie
                    g[current_vertex].append(u)
                    g[u].append(current_vertex)
                else:
                    break
            if bridge:
                # przechodzimy wybraną krawędzią do kolejnego wierzchołka grafu
                # przebytą krawędź usuwamy z grafu
                g[current_vertex].remove(u)
                g[u].remove(current_vertex)
                g.pop(current_vertex)
            cycle.append((current_vertex, u))
        return cycle

