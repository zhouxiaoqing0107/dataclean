import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql import functions
from pyspark.sql.functions import *
import click
from datetime import datetime

#spark配置
def getSparkSession():

    spark=(SparkSession.builder.config('hive.exec,dynamic.partition','true')
    .config('hive.exec.dynamic.partition.mode','nonstrict')
    .enableHiveSupport()
    .getOrCreate()
           )

    sc=spark.sparkContext
    application_id=sc.applicationId
    return spark,application_id

@click.command()

##时间
#统一日期格式为yyyymmdd
def datelist(beginDate,endDate):
    date_1=[datetime.strptime(x,'%Y%m%d') for x in list(pd.date_range(start=beginDate,end=endDate))]
    return date_1

#print(pd.date_range('20180901','20180905'))
#print(pd.date_range('2018-09-01','2018-9-5'))
#print(pd.date_range('2018/09/01','2018/9/5'))
#print(pd.date_range('9/1/2018','9/5/2018'))

d1=date_list('20200921','20200923')

def main():

    spark,application_id=getSparkSession()
    #需要传参
    target_date = xxxx
    sql_1=f"select * from ....where \
    date='{target_date}'"

    #不需要传参
    sql_1 = "select * from ....where \
        date='20220918'"

    #结果展示/储存
    spark.sql(sql_1).show()
    #df=df.toPandas   --spark df --> pandas df

if __name__=='__main__':
    main()



