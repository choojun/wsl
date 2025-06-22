import pyspark.sql.functions as F
from pyspark.sql.functions import udf
from pyspark.sql.types import DoubleType, IntegerType, StringType, ArrayType

class SalesProcessor:
    
    @staticmethod
    @udf(returnType=StringType())
    def format_price(price):
        return f"RM{price:,.2f}"
    
    
    @staticmethod
    @udf(returnType=DoubleType())
    def calculate_discounted_price(unit_price, discount_perc):
        return unit_price * (1 - discount_perc / 100.0) 
    
    
    