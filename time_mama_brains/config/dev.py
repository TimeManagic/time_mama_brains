# dev

config = {
    'VENV': 'dev',
    'SQLALCHEMY_DATABASE_URI': 'postgresql://tencentdb_3501ozmp:o3b%7C!82ax%7BKcG4U@postgres-3501ozmp.sql.tencentcdb.com:50140/tencentdb_3501ozmp',
    # 自动跟踪数据库更改
    'SQLALCHEMY_TRACK_MODIFICATIONS': True,
    # 显示原始查询SQL
    'SQLALCHEMY_ECHO': True,
    # 禁止自动提交数据处理(手动执行commit)
    'SQLALCHEMY_COMMIT_ON_TEARDOWN': False
}
