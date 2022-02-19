# importing the libraries
import pandas as pd

# importing the dataset
udemy_dataset = "C:/Users/HIMANSHU GUPTA/Data analysis folder/udemy_finance_data_analysis/udemy_output_All_Finance__Accounting_p1_p626.csv"
df = pd.read_csv(udemy_dataset)

## data pre-processing ##

# removing with unwanted columns
unwanted_columns = ['id','discount_price__currency','price_detail__currency',
                    'discount_price__price_string','price_detail__price_string','rating',
                    'avg_rating','is_wishlisted','created']
df = df[df.drop(unwanted_columns,axis = 1,inplace = True)]

# renaming the specfic columns.
df = df.rename(columns = {'is_paid':'Price','avg_rating_recent':'Rating','num_subscribers':'Subscribers',
 'num_reviews':'Reviews','num_published_lectures':'Published_lectures',
 'num_published_practice_tests':'Published_practice_tests', 
 'price_detail__amount':'Actual_price','discount_price__amount':'Discount_price',
 'published_time':'Published_date'})

# Price column
def price(x):
    if x == True:
        return 'Paid'
    else:
        return 'Free'
df.Price = df.Price.apply(price)

# filling nan values with zero in discount, actual price columns
df.Discount_price = df.Discount_price.astype('str')
df.Actual_price   = df.Actual_price.astype('str')

df['Discount_price'] = df['Discount_price'].apply(lambda x: x.replace('nan','0'))
df['Actual_price']   = df['Actual_price'].apply(lambda x: x.replace('nan','0'))

df.Discount_price = df.Discount_price.astype('float')
df.Actual_price   = df.Actual_price.astype('float')

# doing slicing in Rating column 
df.Rating = df.Rating.astype('str')
df.Rating = df.Rating.apply(lambda x : x[:3])
df.Rating = df.Rating.astype('float')

# converting Published_date column into datetime datatype
df['Published_date'] = pd.to_datetime(df['Published_date'])

# taking month,year from Published_date column.
df['Month'] = df['Published_date'].dt.month
df['Year']  = df['Published_date'].dt.year
df['Date']  = df['Published_date'].dt.date

# Function for date column.
def month(x):
    if x == 1:
        return 'January'
    elif x == 2:
        return 'February'
    elif x == 3:
        return 'March'
    elif x == 4:
        return 'April'
    elif x == 5:
        return 'May'
    elif x == 6:
        return 'June'
    elif x == 7:
        return 'July'
    elif x == 8:
        return 'August'
    elif x == 9:
        return 'September'
    elif x == 10:
        return 'october'
    elif x == 11:
        return 'November'
    elif x == 12:
        return 'December'
    else: return 'None'
# applying function    
df['Month'] = df['Month'].apply(month)

# year string
df['Year_string'] = df.Year.astype('str')
 
# making new csv file.
df.to_csv(r'C:/Users/HIMANSHU GUPTA/Data analysis folder/udemy_finance_data_analysis/udemy_data_analysis_cleaned_dataset.csv',index=False)
