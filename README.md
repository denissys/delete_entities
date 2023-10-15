# Delete entities from Datastore

This project deletes all entities from the Datastore with the specified kind and filter.

## Requirements

* The gcloud CLI must be installed.
* The Datastore credential file with read and delete permissions must be present in the current working directory.

`export GOOGLE_APPLICATION_CREDENTIALS=credential.json`

* Tutorial of Google Credential: https://developers.google.com/workspace/guides/create-credentials?hl=pt-br


## Setup

To install the project, run the following command:

`python3 setup.py sdist`


## Setting up the environment

To set up the environment, run the following command in the terminal:

### Usage
To delete all entities from the Datastore with the kind of "Card" and the country of "BR", you can use the following command:

`python3 delete_entities/main.py --kind_value Card --param_name country --param_value BR`

This command will delete all entities with the kind of "Card" and the country of "BR".

To specify a different maximum number of retries, you can use the --max_retries argument. For example, to retry the operation 100 times, you can use the following command:

`python3 delete_entities/main.py --kind_value Card --param_name country --param_value BR --max_retries 100`


This command will retry the operation up to 100 times if an error occurs.

## Testing

To run the tests, use the following command:

`python -m unittest tests/test_delete_entities.py`


This command will run the unit tests for the project.

## License

This project is licensed under the MIT License.