# event listener on search feild 'change'
# everytime a change happens we want a fetch request to /cards.json
# as part of the fetch request we have a query string fetch.cards.json = ?${value}
# the route will grab all cards whose name contains that string
# need a crud function to filter by names that contain ""
# route takes data and jsonfiys to return it to js
# .then to json 
# .then((result)) => {
#   for card in cards:
#   insertHTML()
#   <div name=card_container>
# }