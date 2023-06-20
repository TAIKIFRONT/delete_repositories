import requests

def delete_repository(org_name, repo_name, token):
    headers = {
        'Authorization': f'Bearer {token}'
    }

    # リポジトリの削除
    delete_url = f'https://api.github.com/repos/{org_name}/{repo_name}'
    response = requests.delete(delete_url, headers=headers)
    if response.status_code == 204:
        print(f'{repo_name} を削除しました')
    else:
        print(f'{repo_name} の削除に失敗しました')


# 組織名とトークンを設定して実行
ORGANIZATION_NAME = ''  # organizationを入力
TOKEN = ''  # organizationの管理者権限のあるユーザーのトークンを入力

# 削除したいリポジトリ名を指定して個別に削除
delete_repository(ORGANIZATION_NAME, '# ここにリポジトリ名を指定 ', TOKEN)
