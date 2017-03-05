# -*- coding: utf-8 -*-

from monte_carlo import patterns, stock_patterns, connect

if __name__ == "__main__":
    con = connect.Connect()
    con.get_csv()

    patterns = patterns.Patterns()
    patterns.read_data()

    stock = stock_patterns.Stock()
