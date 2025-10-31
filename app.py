#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# 读取HTML文件内容
def get_html_content():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>文件未找到</title>
            <meta charset="UTF-8">
        </head>
        <body>
            <h1>错误：index.html 文件未找到</h1>
            <p>请确保 index.html 文件在当前目录中。</p>
        </body>
        </html>
        """

@app.route('/')
def index():
    """主页路由 - 显示饼干徽章页面"""
    html_content = get_html_content()
    return render_template_string(html_content)

@app.route('/badge')
def badge():
    """徽章页面的别名路由"""
    return index()

@app.route('/health')
def health_check():
    """健康检查接口"""
    return {
        'status': 'healthy',
        'message': '饼干徽章服务运行正常',
        'service': 'Cookie Badge Service'
    }

@app.route('/static/<path:filename>')
def static_files(filename):
    """静态文件服务（如果需要）"""
    return send_from_directory('static', filename)

@app.errorhandler(404)
def not_found(error):
    """404错误处理"""
    return """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>页面未找到</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #8B4513 0%, #D2691E 100%);
                color: white;
                text-align: center;
                padding: 50px;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            h1 { font-size: 3em; margin-bottom: 20px; }
            p { font-size: 1.2em; margin-bottom: 30px; }
            a { 
                color: #FFE4B5; 
                text-decoration: none; 
                font-size: 1.1em;
                padding: 10px 20px;
                border: 2px solid #FFE4B5;
                border-radius: 25px;
                transition: all 0.3s;
            }
            a:hover {
                background: #FFE4B5;
                color: #8B4513;
            }
        </style>
    </head>
    <body>
        <h1>🍪 404</h1>
        <p>哎呀！这个页面不见了，就像被吃掉的饼干一样...</p>
        <a href="/">返回饼干徽章页面</a>
    </body>
    </html>
    """, 404

if __name__ == '__main__':
    print("🍪 启动饼干徽章服务...")
    print("📱 手机访问地址：")
    print("   - 本地访问: http://localhost:5000")
    print("   - 局域网访问: http://你的IP地址:5000")
    print("🔗 可用路由：")
    print("   - / 或 /badge : 饼干徽章页面")
    print("   - /health : 服务健康检查")
    print("⚡ 按 Ctrl+C 停止服务")
    print("-" * 50)
    
    # 启动Flask应用
    # host='0.0.0.0' 允许外部访问（手机可通过局域网IP访问）
    # debug=True 开启调试模式，代码修改后自动重启
    app.run(host='0.0.0.0', port=5000, debug=True)