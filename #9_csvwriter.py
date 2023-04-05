import csv

filename = 'csvwriter0.csv'

clubs = [['Real Madrid', 'Spain', 9.1], ['Napoli', 'Italy', 7.5],['AC Milan', 'Italy', 9.9]]

#Writing clubs[] all at once via writerows()
with open (filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Club','Country', 'Rating'])
    writer.writerows(clubs)

#Writing clubs line by line using writerow()
with open (filename, 'w')as f:
    writer = csv.writer(f)
    writer.writerow(['Club','Country','Rating'])
    for club in clubs:
        writer.writerow(club)