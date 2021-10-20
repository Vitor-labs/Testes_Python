from datetime import datetime
import instaloader

loader = instaloader.Instaloader()
loader.login('u.vito.duarte', 'Zerr0Zerr0')

posts = instaloader.Profile.from_username(
    loader.context, "shit_du_adm").get_posts()

comeco = datetime(2021, 4, 15)
fim = datetime(2021, 5, 20)

for post in posts:
    if (post.date >= comeco) and (post.date <= fim):
        print("DATA: " + str(post.date))
        loader.download_post(post, "baixado")
