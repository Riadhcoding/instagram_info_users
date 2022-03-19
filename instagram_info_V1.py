import requests
username = input('Enter Username: ')
url = f'https://www.instagram.com/{username}/?__a=1'
r = requests.get(url).json()
bio = r['graphql']['user']['biography']
username = r['graphql']['user']['full_name']
profile_pic = r['graphql']['user']['profile_pic_url_hd']
posts = r['graphql']['user']['edge_owner_to_timeline_media']['count']
followers = r['graphql']['user']['edge_followed_by']['count']
following = r['graphql']['user']['edge_follow']['count']
print(f'username: {username}')
print(f'Bio: {bio}')
print(f'Posts: {posts}')
print(f'Followers: {followers}')
print(f'Following: {following}')
pic = requests.get(profile_pic)
with open('profile_pic.png','wb') as f :
    f.write(pic.content)

