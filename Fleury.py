# -*- coding: iso-8859-2 -*-
#
# Fleury's Algorithm implementation
# Dawid Kulig
# dawid.kulig[at]uj.edu.pl

from copy import copy

class Fleury:

    COLOR_WHITE = 'white'
    COLOR_GRAY  = 'gray'
    COLOR_BLACK = 'black'

    def __init__(self):
        pass

    def set_graph(self, graph):
        self.graph = graph

    def run(self):
        print "Running Fleury algorithm for graph : ", self.graph
        print self.fleury(self.graph)

    def is_connected(self, G):
        print G
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
        Funkcja, ktora liczbe nieparzystych krawedzi w grafie
        Returns: lista nieparzystych krawedzi w grafie
        """
        even_degree_nodes = []
        for u in G:
            if len(G[u]) % 2 == 0:
                even_degree_nodes.append(u)
        return even_degree_nodes


    def is_eulerian(self, even_degree_odes, graph_len):
        """
        Funkcja, ktora sprawdza czy podany graf jest grafem Eulerowskim
        Returns: true / false
        """
        return (True if graph_len - len(even_degree_odes) <= 2 else False)


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
            return 'Podany graf nie jest grafem Eulerowskim!'
        else:
            g = copy(G)
            cycle = []
            # wybieramy dowolny wierzcho�ek w grafie o niezerowym stopniu
            u = edn[0]
            while len(self.convert_graph(g)) > 0:
                current_vertex = u
                for u in g[current_vertex]:
                    g[current_vertex].remove(u)
                    g[u].remove(current_vertex)
                    # wybieramy kraw�d�, kt�ra nie jest mostem
                    # (przej�cie przez most oznacza brak mo�liwo�ci powrotu do tego wierzcho�ka
                    # zatem je�li zosta�y w nim nieodwiedzone kraw�dzie, to tych kraw�dzi ju� by�my nie odwiedzili
                    # i cykl Eulera nie zosta�by znaleziony)
                    bridge = not self.is_connected(g)
                    if bridge:
                        # nie ma innego wyboru (krawedz - most)
                        # zapami�tujemy t� kraw�d� na li�cie lub na stosie
                        g[current_vertex].append(u)
                        g[u].append(current_vertex)
                    else:
                        break
                if bridge:
                    # przechodzimy wybran� kraw�dzi� do kolejnego wierzcho�ka grafu
                    # przebyt� kraw�d� usuwamy z grafu
                    g[current_vertex].remove(u)
                    g[u].remove(current_vertex)
                    g.pop(current_vertex)
                cycle.append((current_vertex, u))
        return cycle