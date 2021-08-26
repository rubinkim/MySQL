import pymysql

def get_monthly_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT DATE_FORMAT(sdate, '%m) AS month, SUM(revenue) AS revenue, SUM((profit) AS profit
            FROM sales_book
            GROUP BY `month`
            ORDER BY `month`;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results