import tweepy
import csv
ids=[]
# def get_list(user_name):
#     user_id=user_name
#     consumer_key = 'hnmFlqb9am77jc1kWcFSXUtGT'
#     consumer_secret = 'AXQxBCls220sV0MsFZMfd6smSM5rETfmtRiknC5iHpLPVw83bN'
#     access_token = '1393937841823027201-2dIw4sc5LYQL9X2JdbydZgXi6d32Fu'
#     access_token_secret = '3TuaFx4redeHn4IiCYU1iZ32K47oiO6tfk4qLBSL39aP8'
#     auth = tweepy.OAuthHandler (consumer_key, consumer_secret)
#     auth.set_access_token (access_token, access_token_secret)
#     api = tweepy.API(auth,wait_on_rate_limit=True)
#     for page in tweepy.Cursor(api.followers, screen_name=user_id).pages():
#         ids.append(page)
#         print(len(ids))
#     return ids
#
#
#
# def read_list(name):
#     f = open('/home/solin/twitter_date/'+name+'.csv', 'a+', encoding='utf-8')
#     csv_writer = csv.writer(f)
#     csv_writer.writerow(["姓名", "地点", "描述"])
#     for i in range(len(ids)):
#         list_xr=[]
#         print('Name - ' + ids[i].name)
#         print('Bio - ' + ids[i].description)
#         print('Location - ' + ids[i].location)
#         list_xr.append(ids[i].name)
#         list_xr.append(ids[i].location)
#         list_xr.append(ids[i].description)
#         csv_writer.writerow(list_xr)
#         list_xr.clear()
#
# get_list('DNC')
#
# print(len(ids))
# read_list("DNC")
"""
API Key:
ps5HAs7Q1sH7cFP2SVHvtXn4r
API Secret Key:
hxB8woD1p3jAyn4qd6KFq16zo5gWb480F0VV5r4HkHjE0RwPi4
Bearer Token:
AAAAAAAAAAAAAAAAAAAAAEUEPwEAAAAAu%2FlniOcLbU9S7X7h3WbfXHqQPEA%3DETnoUVgK9EizsIBQkUStE3EGmtv20AyIOmdmWJHPtbSg2KW0bH
Access Token:
1393241582057439241-u0Rgsmco8zwGkG3FkHOPVrdSUr4DOO
Access Token Secret:
bVLW2m89VludbcUZ40KBDsaHuYM8jnW0fj7uCJsiGNR2M
"""
# 消费方密钥（Consumer Key）
# 消费方机密（Consumer Secret）
# 访问令牌密钥（Access Token Key）
# 访问令牌机密（Access Token Secret）
import pandas as pd
consumer_key = 'HE5ZuiHoBpj8Y6yYtWlJFAKAG'
consumer_secret = 'BBcf3qKjalu9fT2Xa1a7t1CRLQmmuTSr4ENrdxHqH2nIqzf8FW'
access_token = '1395176583590146050-gZvwQACAr1LnaktShyYyHKonYgchhB'
access_token_secret = 'Csdma2YiiEbscww9JmjtOwEogzbpwVhW2VcAcNqFWWKu4'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token (access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
def get_user(username):
        for user in tweepy.Cursor(api.followers, screen_name=username).items():
            print(user.screen_name)
            df1 = pd.DataFrame({"screen_name":[user.screen_name],
                           "location":[user.location],
                           "created_time":[user.created_at],
                           "followers_count":[user.followers_count],
                           "id":[user.id],
                           "favourites_count":[user.favourites_count],
                           "description":[user.description]
                           })
            return  df1
if __name__ == '__main__':
    df = pd.read_excel('F:\PycharmProjects\crawl_twiter\scratch\politics_name.xlsx')
    screen_name = df['screen_name'].values
    id_list = []
    user_list = []
    location_list = []
    created_time = []
    followers_count = []
    favourites_count = []
    description = []
    df1 = pd.DataFrame({"screen_name": user_list,
                       "location": location_list,
                       "created_time": created_time,
                       "followers_count": followers_count,
                       "id": id_list,
                       "favourites_count": favourites_count,
                       "description": description
                       })
    for one in list(screen_name):
        print(type(one))
        try:
            df2=get_user(one)
            df=pd.concat([df1,df2])
        except Exception as e:
            print(e)
        df.to_csv("politics_data.csv",encoding="utf-8")


