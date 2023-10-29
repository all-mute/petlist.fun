from data_actions import *

sbc = init()
print(get_all_projects(sbc))

print(get_projects_with_hashtags(sbc, ['#ml', '#backend']))

#test_prj = transform_projects(get_all_projects(sbc))[0]

#print(transform_project_to_dict(test_prj))

list_of_prjs, _ = get_all_projects(sbc)
dummy_prj = list_of_prjs[0]

dummy_prj_dict = transform_project_to_dict(dummy_prj)

print(dummy_prj_dict)
assert 'id' in dummy_prj_dict
del dummy_prj_dict['id']
dummy_prj_dict['name'] = 'testXXX'
print("Before update_project", dummy_prj_dict)

dummy_prj = transform_projects([dummy_prj_dict])[0]

response, error = create_project(sbc, dummy_prj)
print("After create_project", response, error)
zxc_id = response[0].id

response, error = update_project(sbc, zxc_id, dummy_prj)
print("After update_project", response, error)

delete_project(sbc, zxc_id)
print(zxc_id, "deleted")

