import psycopg2, logging
from dynaconf import settings

class DB:
    def __init__(self):
        self.settings = settings
        self.db_host  = self.settings["POSTGRES_HOST"]
        self.db_port  = self.settings["POSTGRES_PORT"]
        self.user     = self.settings["POSTGRES_USER"]
        self.password = self.settings["POSTGRES_PASSWORD"]
        self.dbname   = self.settings["POSTGRES_DB"]
        self.logger   = logging.getLogger(__name__)

    def __enter__(self):
        try:
            self.conn = psycopg2.connect(f"host={self.db_host} port={self.db_port} dbname={self.dbname} user={self.user} password={self.password}")
            self.cur = self.conn.cursor()
            return self
        except Exception as e:
            self.logger.error("Error connecting to the database: %s", e)
            raise e

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()

    def commit(self):
        try:
            self.conn.commit()
        except Exception as e:
            self.logger.error("Error committing transaction: %s", e)
            raise e
        finally:
            self.close()

    def close(self):
        try:
            self.cur.close()
            self.conn.close()
        except Exception as e:
            self.logger.error("Error closing the database connection: %s", e)
            raise e

    def add_comment(self, email, timestamp, comment, content_id):
        try:
            self.cur.execute("INSERT INTO comments (email, date_comment, comment, content_id) VALUES (%s, %s, %s, %s)", (email, timestamp, comment, content_id))
            self.logger.info("Comment added successfully: %s", comment)
        except psycopg2.Error as e:
            self.logger.error("Error adding comment: %s", e)

    def get_comments_by_id(self, content_id):
        try:
            self.cur.execute("SELECT * FROM comments WHERE content_id = %s", (content_id,))
            comments = self.cur.fetchall()
            self.logger.info("Retrieved comments by ID: %s", comments)
            return comments
        except psycopg2.Error as e:
            self.logger.error("Error getting comments by ID: %s", e)
            return []

    def get_comments_by_email(self, email):
        try:
            self.cur.execute("SELECT * FROM comments WHERE email = %s", (email,))
            comments = self.cur.fetchall()
            self.logger.info("Retrieved comments by email: %s", comments)
            return comments
        except psycopg2.Error as e:
            self.logger.error("Error getting comments by email: %s", e)
            return []
