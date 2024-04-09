from flask import Flask, render_template, Response, jsonify
import psutil
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import os

app = Flask(__name__)
# Get the path to the static directory relative to the current script
static_dir = os.path.join(os.path.dirname(__file__), 'static')

# Function to get CPU utilization
def get_cpu_percent():
    return psutil.cpu_percent(interval=0.1)

# Function to get memory utilization
def get_memory_percent():
    return psutil.virtual_memory().percent

# Function to get GPU utilization (assuming NVIDIA GPU)
def get_gpu_percent():
    result = os.popen('nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader').read()
    return int(result.strip().split()[0]) if result else 0

# Function to get network utilization (converted to MB or GB)
def get_network_stats():
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent / (1024 * 1024)  # Convert to MB
    bytes_recv = net_io.bytes_recv / (1024 * 1024)  # Convert to MB
    return bytes_sent, bytes_recv

# Function to generate and save a memory utilization pie chart
def generate_memory_plot():
    labels = ['Used', 'Available']
    memory = psutil.virtual_memory()
    sizes = [memory.used, memory.available]
    colors = ['#ff9999', '#66b3ff']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title('Memory Utilization')
    plt.axis('equal')
    plt.savefig(os.path.join(static_dir, 'memory_plot.png'))

# Function to generate and save a GPU utilization bar chart
def generate_gpu_plot():
    labels = ['GPU']
    gpu_percent = get_gpu_percent()
    sizes = [gpu_percent]
    colors = ['#99ff99']
    plt.bar(labels, sizes, color=colors)
    plt.title('GPU Utilization (%)')
    plt.ylim(0, 100)
    plt.savefig(os.path.join(static_dir, 'gpu_plot.png'))

# Route to provide CPU utilization data as JSON
@app.route('/cpu_data')
def cpu_data():
    cpu_percent = get_cpu_percent()
    return jsonify({'cpu_percent': cpu_percent})

# Route for the home page
@app.route('/')
def home():
    # Generate memory and GPU plots
    generate_memory_plot()
    generate_gpu_plot()

    # Get data for rendering the template
    cpu_percent = get_cpu_percent()
    memory_percent = get_memory_percent()
    gpu_percent = get_gpu_percent()
    bytes_sent, bytes_recv = get_network_stats()

    return render_template('graphed.html',
                           cpu_percent=cpu_percent,
                           memory_percent=memory_percent,
                           gpu_percent=gpu_percent,
                           bytes_sent=bytes_sent,
                           bytes_recv=bytes_recv)

# Route to serve static images
@app.route('/<image_name>.png')
def serve_image(image_name):
    return send_image(f'{image_name}.png')

# Function to send an image
def send_image(filename):
    return Response(open(f'static/{filename}', 'rb'), mimetype='image/png')

# Main function
if __name__ == '__main__':
    # Specify a custom port (e.g., 8000) to run the Flask app on
    app.run(host='127.0.0.1', port=8000, debug=True)