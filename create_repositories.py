import requests
import json


def create_repository(org_name, repo_name, access_token):
    url = f'https://api.github.com/orgs/{org_name}/repos'
    headers = {
        'Authorization': 'token ' + access_token,
        'Accept': 'application/vnd.github.v3+json'
    }

    data = {
        'name': repo_name,  # リポジトリ名
        'auto_init': False,  # リポジトリ作成時にREADME.mdを作成しない場合はFalseに指定
        'description': '',  # リポジトリのdescriptionの指定がない場合は空文字列
        'private': True  # リポジトリをprivateに設定する場合はTrueに指定
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        print('リポジトリが正常に作成されました:', repo_name)
    else:
        print('リポジトリの作成に失敗しました:', repo_name, 'ステータスコード:', response.status_code)


# Organization名、リポジトリ名のリスト、アクセストークンを指定して複数のリポジトリを作成
org_name = ''  # 組織名を入力
repo_names = [
    # ここにリポジトリ名を追加
]

access_token = ''  # orgnizationの管理者権限のあるユーザーのトークン入力


for repo_name in repo_names:
    create_repository(org_name, repo_name, access_token)
