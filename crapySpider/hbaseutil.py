# -*- coding: utf-8 -*-
import happybase


connection = happybase.Connection("47.94.196.111")
# connection.create_table(
#     'mytable',
#     {'cf1': dict(max_versions=10),
#      'cf2': dict(max_versions=1, block_cache_enabled=False),
#      'cf3': dict(),  # use defaults
#     }
# )

table = connection.table('mytable')
table.put(b'row-key', {b'cf1:col1': b'value1',
                       b'cf1:col2': b'value2'})

row = table.row(b'row-key', columns=[b'cf1:col1', b'cf1:col2'])
print(row[b'cf1:col1'])
print(row[b'cf1:col2'])


print (connection.tables())