#!/usr/bin/env python3
"""
Created on March 18 2020

@author: Melchior du Lac
@description: Extract the taxonomy ID from an SBML file

"""
import argparse
import tempfile
import os
import logging
import shutil
import docker


def main(inputfile, output):
    """Call the extractTaxonomy docker to return the JSON file

    :param inputfile: The path to the SBML file
    :param output: The path to the output json file

    :param inputfile: str
    :param output: str

    :rtype: None
    :return: None
	"""
    docker_client = docker.from_env()
    image_str = 'brsynth/extracttaxonomy-standalone:v2'
    try:
        image = docker_client.images.get(image_str)
    except docker.errors.ImageNotFound:
        logging.warning('Could not find the image, trying to pull it')
        try:
            docker_client.images.pull(image_str)
            image = docker_client.images.get(image_str)
        except docker.errors.ImageNotFound:
            logging.error('Cannot pull image: '+str(image_str))
            exit(1)
    with tempfile.TemporaryDirectory() as tmpOutputFolder:
        if os.path.exists(inputfile):
            shutil.copy(inputfile, tmpOutputFolder+'/input.dat')
            command = ['/home/tool_extractTaxonomy.py',
                       '-input',
                       '/home/tmp_output/input.dat',
                       '-output',
                       '/home/tmp_output/output.dat']
            container = docker_client.containers.run(image_str, 
                                                     command, 
                                                     detach=True, 
                                                     stderr=True, 
                                                     volumes={tmpOutputFolder+'/': {'bind': '/home/tmp_output', 'mode': 'rw'}})
            container.wait()
            err = container.logs(stdout=False, stderr=True)
            err_str = err.decode('utf-8')
            if 'ERROR' in err_str:
                print(err_str)
            elif 'WARNING' in err_str:
                print(err_str)
            if not os.path.exists(tmpOutputFolder+'/output.dat'):
                print('ERROR: Cannot find the output file: '+str(tmpOutputFolder+'/output.dat'))
            else:
                shutil.copy(tmpOutputFolder+'/output.dat', output)
            container.remove()
        else:
            logging.error('Cannot find the input file: '+str(inputfile))
            exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser('Extract the t')
    parser.add_argument('-input', type=str)
    parser.add_argument('-output', type=str)
    params = parser.parse_args()
    main(params.input, params.output)
