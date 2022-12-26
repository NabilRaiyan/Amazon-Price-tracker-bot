from bs4 import BeautifulSoup
import smtplib
import requests

my_price = 300.00

headers = {
    "Accept-Language": "en-US,en;q=0.9,bn;q=0.8,id;q=0.7,de;q=0.6,ar;q=0.5",
    "User-Agent": "User-agent using myhttpheader",
}

response = requests.get(
    url="https://www.amazon.com/dp/B0B7P646FD/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0?th=1", headers=headers)

website = response.text

soup = BeautifulSoup(website, "html.parser")
raw_price = soup.find(name="span", class_="a-offscreen")
item_price = float(raw_price.get_text().split("$")[1])

if item_price <= my_price:
    my_email = "email@gmail.com"
    password = "password"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="raiyan66p@gmail.com",
                            msg=f"Subject:CUCKOO price alert\n\nHey! CUCKOO price is now ${item_price},"
                                f" which is less than ${my_price}."
                                f" So, buy it. What are you waiting for? ")
