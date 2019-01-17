"""Network generators."""

import random

import networkx as nx


def pasta_zaidi_rozenblat_graph(
        attr_gen, n, m0, mf, ptf, ptl, lcount=1, gamma=0, th=0.5,
        attribute_weights=None, seed=None):
    """Returns a random graph according to the Pasta-Zaidi-Rozenblat
    combined demographic and structural similarity attachment model.

    A graph of $n$ nodes is grown by attaching new nodes each with $m$
    edges that are preferentially attached to existing nodes with high degree,
    but also to nodes who are more demographically similar.

    Parameters
    ----------
    attr_gen : iterable over dicts
        An iterable/generator yielding dictionaries of demographic attributes
        when propmted, mapping string keys to string or numeric values. String-
        valued attributes are understood to be categorical, while all other
        attributes are treated as numeric attributes (note that the model
        treats ordinal attributes similarly).
    n : int
        Number of nodes
    m0 : int
        The minimal degree of a node in the resulting network.
    mf : int
        The maximal degree of a node in the resulting network.
    ptf : float
        The probability of triad formation.
    ptl : float
        The probability of triad linkage.
    lcount : int, optional
        The number of links added in the triad linkage phase. Defaults to 1.
    gamma : float, optional
        The assortativity parameter; controls the assortative or disassortative
        mixing  among  nodes  based  on  their  degree. Defaults to 0.
    th : float, optional
        The similarity threshold; helps to enforce demographic homophily in the
        network as nodes connect to demographically similar nodes for low
        values of this parameter. Defaults to 0.5.
    attribute_weights : dict, optional
        Custom weights for individual similarity attributes. Defaults to equal
        weights.
    seed : int, optional
        Seed for random number generator (default=None).

    Returns
    -------
    G : Graph

    Raises
    ------
    NetworkXError
        If `m0` and `mf` do not satisfy ``0 <= m0 <= mf < n``. Or, if any of
        `ptf`, `ptl`, `gamma` or `th` is not in [0,1].

    References
    ----------
    .. [1] M. Q. Pasta, F. Zaidi, C. Rozenblat "Generating online social
    networks based on socio-demographic attributes", Journal of Complex
    Networks 2014, 2 (4): 475-494.
    """
    if m0 < 0 or m0 > mf or mf >= n:
        raise nx.NetworkXError(
            "Pasta-Zaidi-Rozenblat network must have 0 <= m0 <= mf < n, while "
            "m0={}, mf={}, n={}".format(m0, mf, n))
    for name, var in [('ptf', ptf), ('ptl', ptl), ('gamma', gamma)]:
        if var < 0 or var > 1:
            raise nx.NetworkXError("Pasta-Zaidi-Rozenblat network must have 0 "
                                   "<= {} <= 1, while {}={}".format(
                                       name, name, var))
    if seed is not None:
        random.seed(seed)
