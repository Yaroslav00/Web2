from flask_restful import Resource, request
from flask import jsonify
import os, signal
from redis import Redis
import rq
import subprocess
from rq.job import Job
from models import *
from app import db
JOB_IDS = set()
def delete_worker():
    try:
        workers = rq.Worker.all(queue=rq.Queue('hull_white_task', connection=Redis.from_url('redis://127.0.0.1:6379')))
        os.kill(workers[-1].pid, signal.SIGINT)
        return 'Worker deleted'
    except: 
        return 'No workers available'

class AddTask(Resource):
    def post(self):
        workers = rq.Worker.all(queue=rq.Queue('hull_white_task', connection=Redis.from_url('redis://127.0.0.1:6379')))
        
        if len(workers) < 5:
            print(len(workers))
            proc = subprocess.Popen(['gnome-terminal --working-directory=/home/yaroslav/Task2WithoutDocker/build/rq_worker -x  rq worker hull_white_task'], shell=True)
                 
        queue = rq.Queue('hull_white_task', connection=Redis.from_url('redis://127.0.0.1:6379'))
        job = queue.enqueue('task.example', 20,result_ttl=20)
        JOB_IDS.add(job.id)
        #delete_worker()
        return jsonify({'id':job.id})


class Progress(Resource):
    def get(self):
        job_id = request.args.get('job_id')
        job = Job.fetch(job_id, connection=Redis.from_url('redis://127.0.0.1:6379'))
        return jsonify({'progress': job.meta.get('progress')})

class LogIn(Resource):
    def post(self):
        print(request.form)
        email = request.form['email']
        password = request.form['password']
        try:
            user = User.query.filter_by(email=email).first()
            print(user)
            if password != user.password:
                return 403
            print(User.encode_auth_token(user.id))
            return jsonify({'token':User.encode_auth_token(user.id).decode('utf-8')})
        except:
            return "User does not exist"


class SignUp(Resource):
    def post(self):
        print(request.form)
        email = request.form['email']
        password = request.form['password']
        admin = request.form.get('admin', False)


        user = User(email, password)
        print(user)
        db.session.add(user)
        db.session.commit()
        print(User.encode_auth_token(user.id))
        return jsonify({'token':User.encode_auth_token(user.id).decode('utf-8'), 'email':user.email})