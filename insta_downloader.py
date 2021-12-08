from datetime import datetime
import instaloader

loader = instaloader.Instaloader()
loader.login('u.vito.duarte', 'Zerr0Zerr0')

posts = instaloader.Profile.from_username(
    loader.context, "hermanos_poster").get_posts()

comeco = datetime(2021, 10, 20)
fim = datetime(2021, 11, 14)

for post in posts:
    if (post.date >= comeco) and (post.date <= fim):
        print("DATA: " + str(post.date))
        loader.download_post(post, "baixado")
