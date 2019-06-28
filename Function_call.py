# Example 2: adds user input and detects intents.

import ibm_watson
class chatbot:
    def __init__(self):
        self.x = 1
        self.service = ibm_watson.AssistantV2(iam_apikey = 'vIbIlzCbNyuoKpZExeFxH8XQ22n2HPX0vQCGO3k7FjpA',version = '2019-02-28',url='https://gateway-lon.watsonplatform.net/assistant/api')
        self.assistant_id = 'c7aad5d0-d30e-4c01-967a-b816dc152fab' 
        self.session_id = self.service.create_session(assistant_id = self.assistant_id).get_result()['session_id']
        

    
    def submit(self,query):

        message_input={'text':''}
        message_input['text'] = query
        result={}
        response = self.service.message(self.assistant_id,self.session_id,input = message_input).get_result()
        if response['output']['intents']:
           result['a']=('Detected intent: #' + response['output']['intents'][0]['intent'])
        if response['output']['generic']:
           if response['output']['generic'][0]['response_type'] == 'text':
               result['b']=(response['output']['generic'][0]['text'])
        return result

                # Prompt for next round of input.
                #user_input = input('>> ')
                #message_input = {
                    #'text': user_input
               # }

        # We're done, so we delete the session.
 #service.delete_session(
 #assistant_id = assistant_id,
 #session_id = session_id
  #  )