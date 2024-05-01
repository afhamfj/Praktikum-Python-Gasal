import instaloader

# Instance of Instaloader class
L = instaloader.Instaloader()

# Provide the Instagram profile URL or the Instagram username
profile_name = input("Enter the profile name: ")
profile = instaloader.Profile.from_username(L.context, profile_name)

# Iterate over each post of the profile
for post in profile.get_posts():
    # Download the post image and videos
    L.download_post(post, target=profile_name)