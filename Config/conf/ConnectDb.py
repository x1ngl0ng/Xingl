
import pymysql


class Database:
    """
    连接数据库，sql中要库名.方法名
    """
    def __init__(self, host, user, password, charset='utf8mb4',port='3306'):
        self.db_config = {
            'host': host,
            'user': user,
            'password': password,
            # 'database': database,
            'charset': charset,
            'port': port
            # 'cursorclass': pymysql.cursors.DictCursor
        }
        self.connection = None

    def connect(self):
        try:
            self.connection = pymysql.connect(**self.db_config)
        except Exception as e:
            print(f"没连上数据库: {e}")
            raise

    def close(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, sqlquery, params=None):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                cursor.execute(sqlquery, params)
                result = cursor.fetchall()
            self.connection.commit()
            return result
        except Exception as e:
            print(f"Error executing query: {e}")
            self.connection.rollback()
            raise
        finally:
            self.close()


# 示例用法
if __name__ == "__main__":
    db = Database(host='192.168.202.132', user='root', password='root')
    select_query = 'SELECT * FROM finance.bankcard'
    result = db.execute_query(select_query)


    # try:
    #     # 插入数据
    #     insert_data_query = '''
    #     INSERT INTO users (name, age) VALUES (%s, %s)
    #     '''
    #     db.execute_query(insert_data_query, ('Alice', 30))
    #     db.execute_query(insert_data_query, ('Bob', 25))
    #
    #     # 查询数据
    #     select_query = 'SELECT * FROM users'
    #     result = db.execute_query(select_query)
    #
    #     for row in result:
    #         print(row)
    #
    # except Exception as e:
    #     print(f"An error occurred: {e}")