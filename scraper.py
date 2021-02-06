import re
import pandas as pd
import instaloader
L = instaloader.Instaloader()
list_data = []
count = 0
# Login or load session
L.login('abdosimo14', 'Aurnowac9737')        # (login)
file1 = open("miami_followers3.txt","r")
for line in file1.readlines():
    # Obtain profile metadata
    try:
        profile = instaloader.Profile.from_username(L.context, line.strip())
        biography =  profile.biography.strip().replace('\n','')
        email = re.search(r'[\w\.-]+@[\w\.-]+', biography)
    
        data=   {           
                            'username': profile.username,
                            "followers" : profile.followers,
                            "followings" : profile.followees,
                            "is_private" : profile.is_private,
                            "external_url":profile.external_url,
                            "is_business_account":profile.is_business_account,
                            "business_category_name":profile.business_category_name,
                            "biography": biography,
                            "email"   : email.group(0),
                            "is_verified":profile.is_verified,
                            "profile_pic_url":profile.profile_pic_url,
                            }
        list_data.append(data)
        print(data)
        count+=1
        print(count)
        
    except:
        continue  


df = pd.DataFrame(list_data)
df.to_csv("data7.csv")