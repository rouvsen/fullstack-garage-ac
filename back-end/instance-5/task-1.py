import datetime as dt

birthday_str = input("Doğum tarixinizi il ay gün şeklinde girin (F.e: 2023 11 08): ")
birthday = dt.datetime.strptime(birthday_str, "%Y %m %d")
now = dt.datetime.now()
diff = now - birthday

seconds = diff.total_seconds() #saniye
minutes = seconds / 60 #deqiqe
hours = minutes / 60 #saat
days = diff.days #gun
months = days / 30 #ay
years = days / 365 #yas

print(f"Siz heyatda "
      f"{seconds:.0f} saniye, "
      f"{minutes:.0f} deqiqe, "
      f"{hours:.0f} saat, "
      f"{days} gün ve {months:.0f} ay "
      f"-dir ki yasayiriniz.")
print(f"Yaşınız {years:.0f} dir.")