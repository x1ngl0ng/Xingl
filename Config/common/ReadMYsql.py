import pymysql
from Config.Base.ApiConfigUrl import APIConfig
def execute_sql_query(sql):
    try:
        # 连接到MySQL数据库
        conn = pymysql.connect(
            host='192.168.202.132',  # 数据库主机地址
            port=3306,  # 数据库端口号，默认为3306
            user='root',  # 数据库用户名
            password='root',  # 数据库密码
            charset='utf8mb4',  # 指定数据库字符集
        )

        # 创建游标对象
        cursor = conn.cursor()

        # 执行SQL查询
        cursor.execute(sql)

        # 获取查询结果
        result = cursor.fetchall()

        # 关闭游标和连接
        cursor.close()
        conn.close()

        # 返回查询结果
        return result

    except pymysql.Error as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    execute_sql_query("SELECT t.* FROM a_lab01_fb710d59e.t_pimperson t WHERE CREATEMAN = '1944DE89-8E28-4D10-812C-CAEEAAE8A927'")
