import requests


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)  # 调用get() 并将URL传递给它，再将响应对象存储在变量r中
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dicts = r.json()
print("Total repositories:", response_dicts['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dicts['items']
print("Repositories returned:", len(repo_dicts))

# 研究第一个仓库
repo_dict = repo_dicts[0]

print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])

"""
# 查看第一个仓库的信息
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
"""