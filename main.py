import scratchattach as scratch3
import demochat

session = scratch3.login("usr", "pwd")
user = session.get_linked_user()
conn = session.connect_cloud("1062443106")
client = scratch3.CloudRequests(conn)

@client.request
def send_message(argument1, argument2):
	print(f"Message received from {argument2}: {argument1}")
	response = demochat.respondto(argument1, argument2)
	return response


@client.request
def ping(user):
	print(f"Connection established with user: {user}")
	return "pong"

@client.request
def check_status():
	return "pong"

@client.event
def on_ready():
        print("ScratchGPT is Ready!")

client.run()


