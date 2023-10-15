import google.cloud.datastore
import logging

logging.basicConfig(level=logging.INFO)

def main():

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
            query = datastore.query(kind='Card')
            query.add_filter("country", "=", "BR")

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
    main()
