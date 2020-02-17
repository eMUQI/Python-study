'''
8-13 用户简介：复制前面的程序 user_profile.py ，在其中调用 build_profile() 来
创建有关你的简介；调用这个函数时，指定你的名和姓，以及三个描述你的键-值对。
'''


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
    'albert', 'einstein', location='princeton', field='physics')
print(user_profile)
pass
