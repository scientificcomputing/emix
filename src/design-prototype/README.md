
The goal is to design a common interface for different KNP-EMI solvers. 


**Notes from 2024 March EMIx Hackathon**
* Recall the finite element terminology: A mesh has cells (codimension 0 entities), facets (codimension 1 entities), edges (codimension 2 entities) and vertics (dimension 0 entities). If d = 2, facets = edges. 
* We take the KNP-EMI equations as a starting-point with the fields: [k]_r, k \in K, \phi_r for r in {i, e}
* We distinguish between the intracellular and the extracellular domains.
* Physical parameters (with units) can be constant, vary between intracellular/extracellular space or vary over the mesh cells.
  - Q1: What is our design for speciying spatially-varying parameters (by geometric coordinates)?
  - Q2: What is our design for specifying regionally varying parameters?
  - Either specify constant, or dictionary (ecs: x, ics: x) or file with mesh markers (diffusivity: "diffusivities.xdmf") 
* Initial condition need to be prescribed for all concentrations and the membrane potential \phi_M = \phi_i - \phi_e
* Domain and subdomain information
  - Map from mesh cell to domain marker: cell_tags (or subdomains) 
  - Map from mesh facet to facet marker: facet_tags (or boundaries or interfaces) 
  - Do we need more maps to distinguish between boundary conditions, ionic models etc, or can we have a single geometry specification and rather add such information at the solver level?
  - Convenient to know what is intracellular and what is extracellular domains; intracellular and extracellular domains are identified by tuples of domain markers 
* Distinguish between physical versus numerical parameters
* How to handle units!
  - Some would like to encourage problem specification to be in SI units
  - Marie suggests that it is the problem specification's responsibility to be in a set of consistent units
  

**Physical description and parameters**


