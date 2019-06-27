# Example 1: sets up service wrapper, sends initial message, and
# receives response.

import ibm_watson

# Set up Assistant service.
service = ibm_watson.AssistantV2(
    iam_apikey = 'vIbIlzCbNyuoKpZExeFxH8XQ22n2HPX0vQCGO3k7FjpA', # replace with API key
    version = '2019-02-28',
    url='https://gateway-lon.watsonplatform.net/assistant/api'
)

assistant_id = 'c7aad5d0-d30e-4c01-967a-b816dc152fab' # replace with assistant ID

# Create session.
session_id = service.create_session(
    assistant_id = assistant_id
).get_result()['session_id']

# Start conversation with empty message.
#response = service.message(
 #   assistant_id,
  #  session_id
#).get_result()

# Print the output from dialog, if any. Supports only a single
# text response.
if response['output']['generic']:
    if response['output']['generic'][0]['response_type'] == 'text':
        print(response['output']['generic'][0]['text'])

# We're done, so we delete the session.
service.delete_session(
    assistant_id = assistant_id,
    session_id = session_id
)
# Initialize with empty value to start the conversation.
message_input = {
    'message_type:': 'text',
    'text': ''
    }

# Main input/output loop
def submit():

	while message_input['text'] != 'quit':

	    # Send message to assistant.
	    response = service.message(
	        assistant_id,
	        session_id,
	        input = message_input
	    ).get_result()

	    # If an intent was detected, print it to the console.
	    if response['output']['intents']:
	        print('Detected intent: #' + response['output']['intents'][0]['intent'])

	    # Print the output from dialog, if any. Supports only a single
	    # text response.
	    if response['output']['generic']:
	        if response['output']['generic'][0]['response_type'] == 'text':
	            print(response['output']['generic'][0]['text'])

	    # Prompt for next round of input.
	    user_input = input('>> ')
	    message_input = {
	        'text': user_input
	    }

# We're done, so we delete the session.
service.delete_session(
    assistant_id = assistant_id,
    session_id = session_id
)