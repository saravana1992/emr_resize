import boto3

cluster_id = "cluster-id"
instance_info = {}
emr_client = boto3.client('emr')

# Listing the Instance Groups of the above cluster Id
instance_groups = emr_client.list_instance_groups(ClusterId=cluster_id)['InstanceGroups']
for each_instance_group in instance_groups:
  if each_instance_group['InstanceGroupType'] == 'CORE' or each_instance_group['InstanceGroupType'] == 'TASK':
    instance_group_id = each_instance_group['Id']
    print(instance_group_id)
    instance_info[instance_group_id]=each_instance_group['RunningInstanceCount']
    emr_client.modify_instance_groups(InstanceGroups=[{'InstanceGroupId':instance_group_id,'InstanceCount':each_instance_group['RunningInstanceCount']-2}])
