from datetime import datetime
import instaloader

loader = instaloader.Instaloader()
loader.login('u.vito.duarte', 'Zerr0Zerr0')

posts = instaloader.Profile.from_username(
    loader.context, "otaku_no_kyojin_").get_posts()

comeco = datetime(2022, 1, 25)
fim = datetime(2022, 1, 23)

for post in posts:
    if (post.date >= comeco) and (post.date <= fim):
        print("DATA: " + str(post.date))
        loader.download_post(post, "baixado")
