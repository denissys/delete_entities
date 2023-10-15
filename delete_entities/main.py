import google.cloud.datastore
import logging
import argparse

logging.basicConfig(level=logging.INFO)

def main(kind_value, param_name, param_value, max_retries):
    """
    Deletes all entities of a specific kind from the Datastore based on the provided filter.

    Args:
        kind_value (str): The kind of the entity in Datastore.
        param_name (str): The field name to filter on.
        param_value (str): The value of the field to filter on.
        max_retries (int): The maximum number of retries.

    Returns:
        None
    """

    count = 0
    retries = 1

    while retries <= max_retries:
        try:
            # Initializes the Datastore client.
            datastore = google.cloud.datastore.Client()

            # Queries for entities based on provided kind and filter.
            query = datastore.query(kind=kind_value)
            query.add_filter(param_name, "=", param_value)

            # Iterates over the entities and deletes them.
            for entity in query.fetch():
                # Uncomment the next line to print the entity for debugging purposes.
                #print(entity)

                # Deletes the entity.
                datastore.delete(entity.key)
                count += 1

                if count % 1000 == 0:
                    logging.info("%d entities deleted so far", count)

            # Breaks out of the loop if everything went well.
            break

        except Exception as e:
            logging.error("Error: %s. Attempt %d of %d", str(e), retries, max_retries)
            retries += 1

    else:
        logging.error("Maximum number of attempts reached!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete entities from Google Cloud Datastore.")
    parser.add_argument("--kind_value", required=True, help="Kind of the entity in Datastore.")
    parser.add_argument("--param_name", required=True, help="Field name to filter on.")
    parser.add_argument("--param_value", required=True, help="Value of the field to filter on.")
    parser.add_argument("--max_retries", type=int, default=100, help="Maximum number of retries.")

    args = parser.parse_args()

    main(args.kind_value, args.param_name, args.param_value, args.max_retries)
