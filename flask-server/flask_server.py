# Python 3.6.8
# for CentOS 7
from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://jimzhou.cn"]}})  # 允许特定域名访问

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get('code', '')
    if not code:
        return jsonify({'error': 'No code provided'}), 400

    try:
        # 使用 stdout=subprocess.PIPE 和 stderr=subprocess.PIPE 兼容旧版本
        result = subprocess.run(
            ['python3', '-c', code],
            stdout=subprocess.PIPE,  # 捕获标准输出
            stderr=subprocess.PIPE,  # 捕获错误输出
            universal_newlines=True,  # 将输出作为字符串处理（旧版本的替代方案）
            timeout=5  # 限制执行时间
        )
        return jsonify({
            'output': result.stdout,  # 返回标准输出
            'error': result.stderr   # 返回错误输出
        })
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Execution timed out'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
