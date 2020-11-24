# extractTaxonomy

* Docker image: [brsynth/extracttaxonomy-standalone](https://hub.docker.com/r/brsynth/extracttaxonomy-standalone)

Tool that parses a GEM SBML model and outputs a JSON with the taxonomy ID of the model

## Input

Required:
* **-input**: (string) Path to the input SBML file

## Output

* **-output**: (string) Path to the output json file

## Dependencies

* Base docker image: [brsynth/rpbase](https://hub.docker.com/r/brsynth/rpbase)

## Installing

To compile the docker use the following command:

```
docker build -t brsynth/extracttaxonomy-standalone:v1 .
```

### Running the test

To run the test, run the following command:

```
python run.py -input test/e_coli_model.sbml -output test/taxonomy.json
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

v0.1

## Authors

* **Melchior du Lac** 
* Thomas Duigou

## License

[MIT](https://github.com/Galaxy-SynBioCAD/rpExtractSink/blob/master/LICENSE)

## Acknowledgments

* Joan Hérisson

### How to cite extractTaxonomy?
