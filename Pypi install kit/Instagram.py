#---Only for Education Purpose---#

import instaloader

nm=input("Enter Username:")

insta=instaloader.Instaloader() # Note-: Second time ma Instaloader() ma I capital avse

# insta.download_profile(nm,profile_pic_only=True)    # For Private profiles
insta.download_profile(nm,profile_pic_only=False)    # Foe Public profile

print("Download Successfull...")