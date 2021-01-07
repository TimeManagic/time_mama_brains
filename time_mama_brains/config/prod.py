# prod

config = {
    'VENV': 'prod',
    'SQLALCHEMY_DATABASE_URI': 'postgresql://tencentdb_3501ozmp:o3b%7C!82ax%7BKcG4U@10.0.0.14:5432/tencentdb_3501ozmp',
    # 自动跟踪数据库更改
    'SQLALCHEMY_TRACK_MODIFICATIONS': True,
    # 显示原始查询SQL
    'SQLALCHEMY_ECHO': False,
    # 禁止自动提交数据处理(手动执行commit)
    'SQLALCHEMY_COMMIT_ON_TEARDOWN': False
}
