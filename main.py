import subprocess, time, pdb
import sys, re, json
import datetime, click
from typing import Tuple, Generator
from pyspark.sql import SparkSession

def gen_labels(labels: str):
    # 解析 labels
    # Input:
    # __name__="scrape_series_added", instance="172.29.1.3:9100", job="worknode"
    
    targets = labels.replace('"','').replace(' ','')
    for target in targets.split(','):
        key, value = target.split('=')
        if key == '__name__':
            yield "metric", value
        else:
            yield key, value

def get_datetime_string(target: int) -> str:
    # 時間戳記轉換成 string 格式為 yyyy-mm-dd
    # Input:
    #   timestamp 
    # output:
    #   yyyy-mm-dd
    tmp = datetime.datetime.fromtimestamp(target)
    return tmp.strftime('%Y-%m-%d')

def parser_data(row: str) -> dict:
    # 解析 prometheus 的資料
    # Input: 
    # {__name__="scrape_series_added", instance="172.29.1.3:9100", job="worknode"} 0 1685342871212
    pattern=r"{(?P<data>.*)} (?P<value>(\S+)) (?P<timestamp>(\S+))"
    tmp = re.match(pattern, row).groupdict()

    output = {key:value for key, value in gen_labels(tmp['data'])}
    output['value'] = tmp['value']
    output['timestamp'] = int(tmp['timestamp'])//1000
    output['date'] = get_datetime_string(output['timestamp'])

    return output

@click.command()
@click.option('--output', '-o', help="--output [PATH/TO/OUTPUT/FOLDER]") # 指定 output 資料夾位置
def main(output):
    data = sys.stdin.read().splitlines() # 螢幕輸入 prometheus 資料
    # 建立 spark session
    spark = (
        SparkSession
          .builder
          .appName("prometheus ETL")
          .master("local[*]")
          .config("spark.driver.maxResultSize", "10g")
          .config("spark.driver.memory", "4g")
          .getOrCreate()
    )

    rdd = spark.sparkContext.parallelize(data) # 將螢幕輸入的資料，放入 rdd 中
    rdd = rdd.map(parser_data) # parser Prometheus 資料
    spdf = rdd.toDF() # 將 rdd 轉換成 dataframe
    # 將資料以 metric 與 date 分類儲存
    (
        spdf.write.option("header", True)
            .partitionBy("metric","date")
            .mode("append")
            .csv(output)
    )

if __name__ == '__main__':

    main()


