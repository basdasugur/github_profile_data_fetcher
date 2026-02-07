import requests


# 1. Setup Target
username = "basdasugur" # -> Github username
url = f"https://api.github.com/users/{username}"

print(f"🕵️‍♀️ Investigating user: {username} ...")
print("-" * 40)

# 2. Send Request 
response = requests.get(url)


# 3. Check Status
if response.status_code == 200:
    print("✅ Target Found! Downloading data ...")
    
    
    # 4. Parse JSON (Veriyi çözümle)
    # Sunucudan gelen karmaşık yazıyı Python Sözlüğüne çevirir.
    profile_data = response.json()
    
    # 5. Extract Specific Info (İstediğimiz bilgileri cımbızla)
    # .get() kullanıyoruz ki veri yoksa hata vermesin.
    my_name = profile_data.get("name")
    my_bio = profile_data.get("bio")
    public_repos = profile_data.get("public_repos")
    followers = profile_data.get("followers")
    location = profile_data.get("location")
    created_at = profile_data.get("created_at")
    
    # 6. Display Report (Raporlar)
    print("\n--- 📄 USER REPORT ---")
    print(f"👤 Name : {my_name}")
    print(f"📝 Bio    : {my_bio}")
    print(f"📍 Location : {location}")
    print(f"📦 Repos : {public_repos}")
    print(f"👥 Followers : {followers}")
    print(f"📅 Created : {created_at}")

else:
    print(f"❌ Error! User not found. Status Code : {response.status_code}")