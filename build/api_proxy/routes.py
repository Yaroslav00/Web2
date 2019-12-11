from app import api
from views import *

# USERS should be placed at sql database with encoded(optional) passwords.
# Both finished tasks and processing task are stored in sql tables too.
api.add_resource(SignUp, '/api/api_proxy/auth/signup/')
api.add_resource(LogIn, '/api/api_proxy/auth/login/')
api.add_resource(AddTask, '/api/api_proxy/add_task/')
api.add_resource(Progress, '/api/api_proxy/progress/')
# In this resources requests to BACKWARD QUEUE should be sent in order to get the 
# api.add_resource(AllFinishedTasks, '/api/api_proxy/finished_tasks/')
# api.add_resource(AllProcessingTasks, '/api/api_proxy/processing_tasks/')


# Waiting for callback
# api.add_resource(Result, '/api/api_proxy/result/')


# some how get progress every ~ 0.5 c (ws)
# That's all!)