import pymysql

def get_monthly_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT DATE_FORMAT(sdate, '%m') AS `month`, 
            SUM(revenue) AS revenue, SUM(profit) AS profit
            FROM sales_book
            GROUP BY `month`
            ORDER BY `month`;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

def get_company_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT scompany, SUM(revenue) as revenue, SUM(profit) AS profit
            FROM sales_book
            GROUP BY scompany
            ORDER BY revenue DESC;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

def get_names_units_company(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT scompany, pname, SUM(sunit) AS unit
            FROM sales_book
            GROUP BY scompany, pname
            ORDER BY scompany, pname;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

def get_product_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT pname, SUM(sunit) AS unit, SUM(revenue) AS revenue, SUM(profit) AS profit
        FROM sales_book
        GROUP BY pname
        ORDER BY pname;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

def get_category_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT pcategory, SUM(revenue) AS revenue, SUM(profit) AS profit
        FROM sales_book
        GROUP BY pcategory
        ORDER BY pcategory;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results