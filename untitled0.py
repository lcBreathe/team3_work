#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:59:32 2024

@author: gentlemanhk
"""

import sqlite3

# 连接到数据库
conn = sqlite3.connect('images.db')
c = conn.cursor()

# 创建表
c.execute('''CREATE TABLE IF NOT EXISTS images
             (id INTEGER PRIMARY KEY, image BLOB)''')

# 提交更改并关闭连接
conn.commit()
conn.close()
from PIL import Image
import sqlite3

# 打开图像文件
image = Image.open('example.jpg')

# 将图像数据转换为字节流
image_data = image.tobytes()

# 连接到数据库
conn = sqlite3.connect('images.db')
c = conn.cursor()

# 将图像数据插入到数据库中
c.execute("INSERT INTO images (image) VALUES (?)", (sqlite3.Binary(image_data),))

# 提交更改并关闭连接
conn.commit()
conn.close()
from flask import Flask, send_file
import sqlite3

app = Flask(__name__)

@app.route('/image/<int:id>', methods=['GET'])
def get_image(id):
    conn = sqlite3.connect('images.db')
    c = conn.cursor()

    # 查询特定id的图像数据
    c.execute("SELECT image FROM images WHERE id=?", (id,))
    image_data = c.fetchone()[0]

    # 关闭连接
    conn.close()

    # 将图像数据作为字节流发送
    return send_file(BytesIO(image_data), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(port=5000)