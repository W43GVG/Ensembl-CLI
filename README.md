# Ensembl-CLI
 ![](https://i.imgur.com/nUnyLWh.png)

 CLI interface for [Ensembl](https://www.ensembl.org) queries

 ## Presentation
 The objective is to implement the possibilities offered by Ensembl's REST API in a command line application.

 ## Use
 ```
 git clone https://github.com/W43GVG/Ensembl-CLI
 ```

 ### Query
 ```
 python ensembl-cli.py COMMANDS
 ```

 #### Get help
 ```
 python ensembl-cli.py COMMAND --help
 ```

 #### Ontologies
 Multiple ontologies can be obtained ([gene ontology](http://www.geneontology.org/): `GO`, [sequence ontology](http://www.sequenceontology.org/): `SO`, [protein ontology](https://proconsortium.org/): `PR`, [uberon](https://uberon.github.io/): `UBERON`). 

 ```
 python ensembl-cli.py onto_id 0000370 SO json
 ```

 ![First lines of the output](https://i.imgur.com/SjbVHOi.png)

 Search ontological terms:

 ```
 python ensembl-cli.py onto_name TERM FORMAT
 ```

 Example:

 ```
 python ensembl-cli.py onto_name tubulin json
 ```

 ## License, notes
 W43GVG under the MIT License.

 Yates, Andrew et al. “The Ensembl REST API: Ensembl Data for Any Language.” Bioinformatics 31.1 (2014): 143–145.