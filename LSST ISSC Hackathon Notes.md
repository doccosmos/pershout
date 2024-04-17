Here are some basic ideas for the LSST ISSC Hackathon:

The project is to work with irregularly sampled time series - we'll assume univariate for the time being (single photometry filter) - and look for outliers. One possible method is:

1) Create persistence diagrams for each time series using a watershed algorithm - some libraries will do this already
2) Calculate the distance between persistence diagrams to create a distance matrix for a set of time series
3) Learn a manifold for the distance matrix
4) Identify points (time series) far from the manifold

An alternate idea might be create a point data cloud for a set of time series - essentially defining some similarity/distance metric between points - and then identifying regions of the point data cloud which are topologically different than others, i.e., define some measure of local topology, e.g., local homology, over some scale.
