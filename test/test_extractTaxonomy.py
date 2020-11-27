import unittest
import tempfile
import os
import sys
import json

sys.path.insert(0, '..')

import rpTool
#WARNING: Need to copy a version of rpSBML locally
import rpSBML

class TestRPextractsink(unittest.TestCase):
    
    def test_getTaxon(self):
        with tempfile.TemporaryDirectory() as tmp_output_folder:
            rpTool.getTaxon(os.path.join('data', 'model.xml'), os.path.join(tmp_output_folder, 'tmp.json'))
            tax_json = json.load(open(os.path.join(tmp_output_folder, 'tmp.json')))
            self.assertTrue(tax_json['taxonomy'][0]=='511145')
