import os
import pandas as pd

# os.chdir(r"")

data = pd.read_excel(r"/Users/nol/PycharmProjects/flaskProject1/test/供应商余额表列表20234211613.xls")
data.head()
html_table = data.to_html('test.html')