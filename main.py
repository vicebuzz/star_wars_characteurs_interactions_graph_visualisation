import json
import networkx as nx
import matplotlib.pyplot as plt

class InteractionGraph():

    def __init__(self):

        self.file = str()
        self.characteurs = list()
        self.data = dict()
        self.graph = nx.Graph()
        

    def getCharacteurs(self):
        # method to get characteurs and create a node for each of them
        for node in self.data['nodes']:
            self.characteurs.append(node['name'])
            self.graph.add_node(node['name'])

    
    def loadData(self, filename):
        # method to load data from filename
        with open(f'archive/{filename}', 'r') as file:
            self.data = json.load(file)


    def main(self):
        self.getCharacteurs()
        # loop through list of interactions and append edges to the graph if it doesn't exist
        for interaction in self.data['links']:
            if not nx.is_path(self.graph, [interaction['source'], interaction['target']]):
                self.graph.add_edge(self.characteurs[interaction['source']], self.characteurs[interaction['target']])

        nx.draw(self.graph, with_labels=True)
        plt.show()
        

if __name__ == '__main__':
    ig = InteractionGraph()
    ig.loadData('starwars-episode-6-interactions.json')
    ig.main()