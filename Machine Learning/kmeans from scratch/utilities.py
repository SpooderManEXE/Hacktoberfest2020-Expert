
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.cm as cm


class RibosomeGene:
    def __init__(self, accession, header, sequence):
        self.accession = accession
        self.name = header
        self.sequence = sequence
        self.length = len(sequence)



def import_16s_sequences():
    with open('ribosome_genes.fasta', 'r') as fp:
        lines = fp.readlines()
        lines = [line.rstrip('\n') for line in lines]
    
    ribosome_gene_list = []
    accession = ''
    header = ''
    sequence = ''
    for line in lines:
        if line.startswith('>'):
            if sequence != '':
                new_gene = RibosomeGene(accession, header, sequence)
                ribosome_gene_list.append(new_gene)
            accession, header = line.lstrip('>').split(', ')
            sequence = ''
        else:
            sequence += line

    new_gene = RibosomeGene(accession, header, sequence)
    ribosome_gene_list.append(new_gene)
    ribosome_gene_list.sort(key=lambda x: x.accession)
    return ribosome_gene_list


def print_distance_matrix(dist):
    """
    Pretty-print a distance matrix.
    """
    genes = sorted(dist.keys())

    for s in [''] + genes:
        print("{: >6}".format(s[:4]), end='')
    print()

    for key1 in genes:
        print("{:6}".format(key1[:4]), end='')
        for key2 in genes:
            value = dist[key1][key2]
            if value is None:
                print("      None", end='')
            else:
                print("{: >#6.1f}".format(dist[key1][key2]), end='')
        print()       


def heatmap(distance_matrix1, distance_matrix2):
    accessions1 = ['EF_A', 'EF_B', 'EF_C', 'EF_D', 'EC_A', 'SD_A', 'SS_A', 'MI_A', 'EC_B', 'EC_C', 'EC_G', 'EC_D', 'EC_E', 'SF_A', 'SS_B', 'EC_F', 'HS_A']
    accessions2 = ['EF_A', 'EF_B', 'EF_C', 'EF_D', 'EC_A', 'SD_A', 'SS_A', 'MI_A', 'EC_B', 'EC_C', 'EC_G', 'EC_D', 'EC_E', 'SF_A', 'SS_B', 'EC_F', 'HS_A']
    accessions1.sort()
    accessions2.sort()
    assert(distance_matrix1 != distance_matrix2)
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 6), dpi=80)
    df1 = pd.DataFrame(data=distance_matrix1, index=accessions1, columns=accessions1)
    df2 = pd.DataFrame(data=distance_matrix2, index=accessions2, columns=accessions2)
    sns.heatmap(df1, cmap="Reds", vmax=150, ax=ax0, square=True, cbar=False)
    sns.heatmap(df2, cmap="Reds", vmax=150, ax=ax1, square=True, cbar=False)
    ax0.set_title('kmer distance matrix')
    ax1.set_title('smith-waterman alignment score matrix')
    plt.show()


def distance_matrix_to_coordinates_MDS(matrix):
    embedding = MDS(n_components=2)
    np_arr = convert_to_numpy_array(matrix)
    matrix_2dims = embedding.fit_transform(np_arr)
    return matrix_2dims


def convert_to_numpy_array(matrix):
    keys = list(matrix.keys())
    keys.sort()
    dim = len(keys)

    the_arr = np.zeros((dim, dim), dtype=float)
    for i in range(dim):
        for j in range(dim):
            distance = matrix[keys[i]][keys[j]]
            the_arr[i, j] = distance
    
    return the_arr


def mds_scatterplot(mds_matrix):
    ribosome_genes = import_16s_sequences()
    gene_names = [x.name for x in ribosome_genes]
    x_coords = [x[0] for x in mds_matrix]
    y_coords = [x[1] for x in mds_matrix]
    rng = np.random.RandomState(0)
    colors = rng.rand(17)
    fig, ax = plt.subplots(figsize=(12, 12))
    #plt.figsize(12, 12)
    ax.scatter(x_coords, y_coords, label=gene_names, c=colors, cmap='viridis')
    for i, accession in enumerate(gene_names):
        ax.annotate(accession, (x_coords[i] + 5, y_coords[i] + 5))
    plt.show()


def initialise_centroids(data, k):
    d = len(data[0])
    minvals = np.min(data, axis=0)
    maxvals = np.max(data, axis=0)
    centroids = np.random.uniform(low=minvals, high=maxvals, size=(k, d))
    return [tuple(c) for c in centroids]


def assign_points(centroids, data):   
    closest_centroids = []
    for p in data:
        distances = [euclidean_distance(p, c) for c in centroids]
        closest_centroids.append(distances.index(min(distances)))
        
    return closest_centroids


def euclidean_distance(a, b):
    """
    Assuming that a and b are each tuples representing points, 
    calculate the euclidean distance beween them.
    """
    return np.linalg.norm(np.array(a) - np.array(b))


def calculate_mean_centroids(data, assignments, k):
    centroids = []
    for cluster in range(k):
        points = [point for point, assignment in zip(data, assignments) if assignment == cluster]
        centroids.append(average_point(points))
        
    return centroids


def average_point(points):
    """
    Take in a list of points, where each point is a tuple.
    Return the average of the points.
    """
    try:
        return tuple(np.mean(np.array(points), axis=0))
    except TypeError:
        return points


def points_equal(centroids1, centroids2):
    """
    Given two lists of points, check that they are equal.
    Allow a floating-point error of epsilon along each dimension.
    """
    epsilon = 0.001
    return np.all(np.array(centroids1) - np.array(centroids2) < epsilon)


def plot_kmeans(data, centroids, assignments, k):
    for cluster in range(k):
        cluster_points = [p for (p, assignment) in zip(data, assignments) 
                            if assignment == cluster]
        x_values = [x for (x, y) in cluster_points]
        y_values = [y for (x, y) in cluster_points]
        plt.scatter(x_values, y_values)
    centroid_x_values = [x for (x, y) in centroids]
    centroid_y_values = [y for (x, y) in centroids]
    plt.scatter(centroid_x_values, centroid_y_values, marker='x', s=80, c='k')
    plt.show()


def print_silhouette_score(data, assignments, label):
    score = silhouette_score(data, assignments)
    print('\nsilhouette score for {}: {:0.2f}'.format(label, score))
