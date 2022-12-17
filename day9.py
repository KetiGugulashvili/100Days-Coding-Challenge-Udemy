# Blind Auction
from replit import clear
bidders_bids = {}
highest_bid = 0
highest_bidder = ''
while True:
    bidder = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    bidders_bids[bidder] = bid
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = bidder
    stop_bidding = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if stop_bidding == "no":
        break
    clear()

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

# exercise 1
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

for i in student_scores:
    if 91 <= student_scores[i] <= 100:
        student_scores[i] = "Outstanding"
    elif 81 <= student_scores[i] <= 90:
        student_scores[i] = "Exceeds Expectations"
    elif 71 <= student_scores[i] <= 80:
        student_scores[i] = "Acceptable"
    elif student_scores[i] <= 70:
        student_scores[i] = "Fail"

print(student_scores)

# exercise 2
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, visits, cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities
    })


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
