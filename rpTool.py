#!/usr/bin/env python3

import rpSBML
import json

def getTaxon(sbml_path, output_path):
    """Return the Taxonomy id from an SBML file

    :param sbml_path: The path to the SBML file
    :param output_path: The path to the output json file

    :type sbml_path: str
    :type output_path: str

    :rtype: None
    :return: None
    """
    rpsbml = rpSBML.rpSBML('tmp')
    rpsbml.readSBML(sbml_path)
    taxon_dict = rpsbml.readTaxonAnnotation(rpsbml.model.getAnnotation())
    try:
        host_taxonomy_id = int(taxon_dict['taxonomy'][0])
    except (ValueError, KeyError) as e:
        taxon_dict = {'taxonomy': ['-1']}
    with open(output_path, 'w') as f:
        json.dump(taxon_dict, f)  
