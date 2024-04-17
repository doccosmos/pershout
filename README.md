# pershout
This is somewhat of a catchall repository for various experiments over the years on outlier detection via persistent homology. This includes:

   * using a similarity metric between time series to evaluate a distance matrix for a data set and then constructing the 1-D topological skeleton using a minimal spanning tree from which outliers are the least connected data points
   * fitting Gaussian processes to time series and then evaluating the distance matrix for a data set using the Wasserstein metric and constructing the persistence diagram from this
   * constructing persistence diagrams for individual time series and then evaluating a distance matrix for a data set and determining outliers from this


