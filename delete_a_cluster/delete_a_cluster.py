#Delete a cluster
import sys
import os
sys.path.append(os.path.abspath(__file__ + '/../../'))
from Utils.utils import Utils
import pprint

class DeleteCluster:
    def __init__(self):
        print('Delete Cluster')
        self.utils = Utils(sys.argv)
        self.hostname = sys.argv[1]
        self.cluster_id = sys.argv[4]


    def delete_cluster(self):
        data = {"markForDeletion" : True}
        delete_cluster_url = 'https://'+self.hostname+'/v1/clusters/'+self.cluster_id
        self.utils.patch_request(data,delete_cluster_url)
        response = self.utils.delete_request({},delete_cluster_url)
        task_id = response['id']
        task_url = 'https://'+self.hostname+'/v1/tasks/'+task_id
        print ("Cluster deletion Status:" + self.utils.poll_on_id(task_url,True))

if __name__== "__main__":
    DeleteCluster().delete_cluster()
