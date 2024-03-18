
The goal is to design a common interface for different KNP-EMI solvers.

Notes 
* A mesh has cells (codimension 0 entities), facets (codimension 1 entities), edges (codimension 2 entities) and vertics (dimension 0 entities). If d = 2, facets = edges. 
* Take the KNP-EMI equations as a starting-point [k]_r, k \in K, \phi_r for r in {i, e} 
* Physical parameters (with units), constant, or regionally or spatially-varying.
  - Constants: gas and Faraday's constant
* Initial conditions for all concentrations and the membrane potential \phi_M = \phi_i - \phi_e
* Domain and subdomain information
  - Map from mesh cell to domain marker  
  - Map from mesh facet to facet marker
* How to handle units!  

**Physical description and parameters**


