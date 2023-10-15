import google.cloud.datastore
import logging
import argparse

logging.basicConfig(level=logging.INFO)

def main(kind_value, param_name, param_value, max_retries):

    """
    Deletes all cards from the Datastore with the country of Brazil.

    Args:
        None

    Returns:
        None
    """

    count = 0
    max_retries = 100
    retries = 1

    while retries < max_retries:
        try:
            """
            Initializes the Datastore client.

            Args:
                None

            Returns:
                A Google Cloud Datastore client
            """
            datastore = google.cloud.datastore.Client()

            """
            Queries for all cards with the country of Brazil.

            Args:
                None

            Returns:
                A Datastore query
            """
            query = datastore.query(kind=kind_value)
            query.add_filter(param_name, "=", param_value)

            """
            Iterates over the entities and deletes them.

            Args:
                entity: A Datastore entity

            Returns:
                None
            """
            for entity in query.fetch():
                """
                Print the entity for debugging purposes.

                Args:
                    entity: A Datastore entity

                Returns:
                    None
                """
                #print(entity)

                """
                Deletes the entity.

                Args:
                    entity: A Datastore entity

                Returns:
                    None
                """
                datastore.delete(entity.key)
                count += 1

                if count % 1000 == 0:
                    logging.info("%s deleted", str(e), count)

            """
            Breaks out of the loop if everything went well.

            Args:
                None

            Returns:
                None
            """
            break

        except Exception as e:
            """
            Print the error and retry.

            Args:
                e: The exception

            Returns:
                None
            """
            logging.error("Erro: %s. Attempt %d of %d", str(e), retries, max_retries)

            retries += 1

    else:
        """
        Print an error message if the maximum number of retries was reached.

        Args:
            None

        Returns:
            None
        """
        logging.error("Maximum number of attempts reached!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete entities from Google Cloud Datastore.")
    parser.add_argument("--kind_value", required=True, help="Kind of the entity in Datastore.")
    parser.add_argument("--param_name", required=True, help="Field name to filter on.")
    parser.add_argument("--param_value", required=True, help="Value of the field to filter on.")
    parser.add_argument("--max_retries", type=int, default=100, help="Maximum number of retries.")

    args = parser.parse_args()

    main(args.kind_value, args.param_name, args.param_value, args.max_retries)