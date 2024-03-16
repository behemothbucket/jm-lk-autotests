import os
import psycopg2
from dotenv import load_dotenv
from utils.webdriver.logger import logger


class SQL:
    @staticmethod
    def get_db_credentials() -> dict:
        load_dotenv()
        return {
            "host": os.getenv("HOST_JM"),
            "port": os.getenv("PORT_JM"),
            "database": os.getenv("DATABASE_JM"),
            "user": os.getenv("USER_JM"),
            "password": os.getenv("PASSWORD_JM"),
        }

    @staticmethod
    def request(query: str, val: tuple | str):
        conn = None
        try:
            params = SQL.get_db_credentials()

            logger.info("-------------Подключение к PostgreSQL...")
            conn = psycopg2.connect(**params)

            logger.info(f"\nИсполняю запрос:\n\n{query}\nСо значениями:\n{val}\n")

            cur = conn.cursor()

            cur.execute(query, (val,))

            result = cur.fetchone()

            return result
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(error)
        finally:
            if conn is not None:
                conn.close()
                logger.info("Закрываю подключение к PostgreSQL-------------")

    @staticmethod
    def get_application_status(app_id: str):
        query = "SELECT status_id FROM application WHERE id = %s"
        val = app_id
        return SQL.request(
            query=query,
            val=val,
        )

    @staticmethod
    def update_app_status(status: int, app_id: str):
        query = "UPDATE application SET status_id = %s WHERE id = %s"
        val = (status, app_id)
        return SQL.request(
            query,
            val,
        )

    @staticmethod
    def log(result, text: str = "") -> None:
        if text:
            logger.info(text.format("\n".join(str(i) for i in result)))
        else:
            "".join(str(i) for i in result)
